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
   git clone <repository-url>
   cd backend-takehome

2. Install dependencies using Poetry:
   poetry install

3. Activate the Poetry environment:
   poetry shell

# Usage

1. Fetch papers from PubMed and display results in the terminal:
   poetry run get-papers-list "your search query"

2. Save the results to a CSV file:
   poetry run get-papers-list "your search query" -f results.csv

3. Enable debug mode:
   poetry run get-papers-list "your search query" -d

# Example

1. poetry run get-papers-list "Machine Learning in Healthcare" -f output.csv
   (This will fetch research papers related to "Machine Learning in Healthcare" and save them in output.csv.)

# Dependencies

This project uses the following libraries:

1. requests - For making API requests.

2. pandas - For handling tabular data.

3. argparse (Built-in Python module) - For parsing CLI arguments.

# License

This project is licensed under the MIT License.
