# Google Careers Page Parser

This script is designed to parse job listings from the Google Careers page.

## Requirements

- Requests
- BeautifulSoup4

## Usage

1. Install the required packages:
   ```bash
   pip install requests beautifulsoup4
   ```

2. Run the script:
   ```bash
   python google_parser.py
   ```

## Code

import requests
from bs4 import BeautifulSoup

# Function to get job listings
def get_job_listings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = []
    
    # Find the job listings
    for job in soup.find_all('div', class_='job-listing'):
        title = job.find('h2').text
        link = job.find('a')['href']
        jobs.append({'title': title, 'link': link})
    
    return jobs

# Main function
if __name__ == '__main__':
    url = 'https://careers.google.com/jobs/'
    job_listings = get_job_listings(url)
    
    for job in job_listings:
        print(f"Job Title: {job['title']} - Link: {job['link']}")