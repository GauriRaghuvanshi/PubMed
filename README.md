# Backend Takehome Project

# Overview 

This CLI tool fetches research papers from PubMed based on a given query, extracts details, and filters out non-academic authors (authors not affiliated with universities or colleges). The results can be displayed in the terminal or saved as a CSV file. 

# Features

1. Fetches research papers from PubMed using the Entrez API.

2. Extracts paper details such as title, publication date, and author information.

3. Filters out non-academic authors based on their affiliations.

4. Saves results in a CSV file for further analysis.

# Installation

1. Ensure you have Python 3.13.2 installed on your system.

# Steps

1. Clone the repository:
   - git clone <repository-url>
   - cd backend-takehome

2. Install dependencies using Poetry:
   - poetry install

3. Activate the Poetry environment:
   - poetry shell

# Usage

1. Fetch papers from PubMed and display results in the terminal:
   - poetry run get-papers-list "your search query"

2. Save the results to a CSV file:
   - poetry run get-papers-list "your search query" -f results.csv

3. Enable debug mode:
   - poetry run get-papers-list "your search query" -d

# Example

1. poetry run get-papers-list "Machine Learning in Healthcare" -f output.csv
   - (This will fetch research papers related to "Machine Learning in Healthcare" and save them in output.csv.)

# Dependencies

- This project uses the following libraries:

1. requests - For making API requests.

2. pandas - For handling tabular data.

3. argparse (Built-in Python module) - For parsing CLI arguments.

# Technologies Used

- This project leverages a combination of widely adopted tools and frameworks to enhance functionality and efficiency:

1. Python: Utilized for scripting and automation. 
- https://www.python.org/

2. Requests: Used for handling HTTP requests efficiently. 

3. Pandas: Assisted in structuring and managing tabular data. 

4. Poetry: Streamlined dependency management and packaging. 

5. PubMed Entrez API: Accessed for fetching research data. 
- https://www.ncbi.nlm.nih.gov/books/NBK25500/

- These technologies were integrated strategically to improve workflow efficiency and data handling while ensuring modular and scalable implementation.

6. LLM Tool - ChatGPT

1. Issue: PowerShell script execution is restricted, preventing venv\Scripts\activate from running.
- Solution: Used Set-ExecutionPolicy Unrestricted -Scope Process to temporarily allow script execution.
- https://chatgpt.com/share/67e6686e-486c-800d-be11-cda308896cbc

2. Issue: VS Code's Pylance couldn't detect Pandas due to environment mismatch.
- Solution: Installed Pandas in the correct environment and selected the appropriate Python interpreter in VS Code.
- https://chatgpt.com/share/67e668b2-12d0-800d-a86b-d7264438715d


# License

- This project is licensed under the MIT License.
