import sys

from bs4 import BeautifulSoup
import requests

def find_jobs(language: str) -> None:
    url = "https://www.juniors.ro/jobs?q=" + language
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    jobs = soup.find_all('li', attrs={'class': 'job'})
    for job in jobs:

        job_elem = job.find('div', attrs={'class': 'job_header_title'})
        title_element = job_elem.find('h3')
        job_name = title_element.get_text(strip=True)
        print("Job Title: " + job_name)

        job_requirements = job.find('ul', attrs={'class': 'job_requirements'})
        company_element = job_requirements.find('strong')
        company_name = company_element.next_sibling.strip()
        print("Company Name: " + company_name)

        location_elem = job.find('div', attrs={'class': 'job_header_title'})
        location_time =  location_elem.find('strong').get_text(strip=True)
        parts = location_time.split('|')
        location = parts[0].strip()
        post_date = parts[1].strip()
        print("Location: " + location)
        print("Post-Date: " + post_date)

        job_tags_elem = job.find('ul', attrs={'class': 'job_tags'})
        job_tags = job_tags_elem.find_all('li')
        print("Job Tags: ", end='')
        for job_tag in job_tags:
            job_tag_elem = job_tag.find('a')
            job_tag_name = job_tag_elem.get_text(strip=True)
            print(job_tag_name + " ", end='')

        print('\n')


if __name__ == '__main__':
   language = sys.argv[1]
   find_jobs(language)