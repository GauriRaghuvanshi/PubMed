import requests
import pandas as pd
import argparse
import json

# Constants for PubMed API
PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"


def fetch_papers(query, debug=False):
    """Fetch research papers from PubMed API based on a query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10  # Fetch top 10 results for now
    }
    
    if debug:
        print(f"Fetching papers with query: {query}")

    response = requests.get(PUBMED_API_URL, params=params)
    response.raise_for_status()  # Raises an error if request fails

    data = response.json()
    if debug:
        print(f"API Response: {json.dumps(data, indent=2)}")

    return data["esearchresult"]["idlist"]


def fetch_paper_details(paper_ids, debug=False):
    """Fetch details of papers given their PubMed IDs."""
    if not paper_ids:
        return []

    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json"
    }
    
    if debug:
        print(f"Fetching details for PubMed IDs: {paper_ids}")

    response = requests.get(PUBMED_SUMMARY_URL, params=params)
    response.raise_for_status()

    data = response.json()
    if debug:
        print(f"Paper Details Response: {json.dumps(data, indent=2)}")

    return data["result"]


def filter_non_academic_authors(paper_details, debug=False):
    """Identify non-academic authors using heuristics."""
    results = []

    for paper_id, details in paper_details.items():
        if paper_id == "uids":
            continue  # Skip metadata

        title = details.get("title", "N/A")
        pub_date = details.get("pubdate", "N/A")
        author_list = details.get("authors", [])

        non_academic_authors = []
        company_affiliations = []
        corresponding_author_email = []

        for author in author_list:
            affiliation = author.get("affiliation", "")
            if "university" not in affiliation.lower() and "college" not in affiliation.lower():
                non_academic_authors.append(author.get("name", "Unknown"))
                company_affiliations.append(affiliation)

        results.append([paper_id, title, pub_date, ", ".join(non_academic_authors), ", ".join(company_affiliations), ", ".join(corresponding_author_email)])
    
    if debug:
        print(f"Filtered Non-Academic Authors: {results}")

    return results


def save_to_csv(results, filename):
    """Save results to a CSV file."""
    df = pd.DataFrame(results, columns=["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"])
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")


if __name__ == "__main__":
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
        print(pd.DataFrame(filtered_results, columns=["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"]))
