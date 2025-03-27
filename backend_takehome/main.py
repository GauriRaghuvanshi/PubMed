import requests
import pandas as pd
import argparse
import json

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_papers(query, debug=False):
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": 10}
    if debug:
        print(f"Fetching papers with query: {query}")
    
    response = requests.get(PUBMED_API_URL, params=params)
    response.raise_for_status()
    
    data = response.json()
    if debug:
        print(f"API Response: {json.dumps(data, indent=2)}")

    return data["esearchresult"]["idlist"]

def fetch_paper_details(paper_ids, debug=False):
    if not paper_ids:
        return []
    
    params = {"db": "pubmed", "id": ",".join(paper_ids), "retmode": "json"}
    if debug:
        print(f"Fetching details for PubMed IDs: {paper_ids}")
    
    response = requests.get(PUBMED_SUMMARY_URL, params=params)
    response.raise_for_status()
    
    data = response.json()
    if debug:
        print(f"Paper Details Response: {json.dumps(data, indent=2)}")

    return data["result"]

def filter_non_academic_authors(paper_details, debug=False):
    results = []
    for paper_id, details in paper_details.items():
        if paper_id == "uids":
            continue

        title = details.get("title", "N/A")
        pub_date = details.get("pubdate", "N/A")
        author_list = details.get("authors", [])

        non_academic_authors = []
        company_affiliations = []

        for author in author_list:
            affiliation = author.get("affiliation", "")
            if "university" not in affiliation.lower() and "college" not in affiliation.lower():
                non_academic_authors.append(author.get("name", "Unknown"))
                company_affiliations.append(affiliation)

        results.append([paper_id, title, pub_date, ", ".join(non_academic_authors), ", ".join(company_affiliations)])

    if debug:
        print(f"Filtered Non-Academic Authors: {results}")

    return results

def save_to_csv(results, filename):
    df = pd.DataFrame(results, columns=["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)"])
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed")
    parser.add_argument("query", help="Search query for PubMed")
    parser.add_argument("-f", "--file", help="Filename to save the results (CSV)")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    print("Fetching papers...")
    paper_ids = fetch_papers(args.query, args.debug)
    paper_details = fetch_paper_details(paper_ids, args.debug)
    filtered_results = filter_non_academic_authors(paper_details, args.debug)

    if args.file:
        save_to_csv(filtered_results, args.file)
    else:
        print(pd.DataFrame(filtered_results, columns=["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)"]))

if __name__ == "__main__":
    main()
