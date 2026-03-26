import requests
from bs4 import BeautifulSoup

class AmazonCareerParser:
    def __init__(self, url):
        self.url = url

    def fetch_page(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f'Failed to fetch page: {response.status_code}')

    def parse_jobs(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        job_cards = soup.find_all('div', class_='job-card')
        jobs = []
        for card in job_cards:
            title = card.find('h2').text.strip()
            location = card.find('span', class_='location').text.strip()
            jobs.append({'title': title, 'location': location})
        return jobs

    def get_jobs(self):
        html = self.fetch_page()
        return self.parse_jobs(html)

# Usage:
# parser = AmazonCareerParser('https://www.amazon.jobs/en/locations')
# jobs = parser.get_jobs()
# print(jobs)
