import sys

from bs4 import BeautifulSoup
import requests

def remove_diacritics(text:str)->str:
    for char in text:
        if char == 'ș':
            text = text.replace(char, 's')
        elif char == 'ț':
            text = text.replace(char, 'ț')
        elif char == 'î':
            text = text.replace(char, 'i')
        elif char == 'ă':
            text = text.replace(char, 'a')
        elif char == 'â':
            text = text.replace(char, 'a')
    return text


def find_jobs(language: str, location_wanted: str) -> None:
    url = "https://www.juniors.ro/jobs?q=" + language
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    jobs = soup.find_all('li', attrs={'class': 'job'})
    cnt = 0
    for job in jobs:

        location_elem = job.find('div', attrs={'class': 'job_header_title'})
        location_time = location_elem.find('strong').get_text(strip=True)
        parts = location_time.split('|')
        location = parts[0].strip()
        post_date = parts[1].strip()

        if location_wanted is None or remove_diacritics(location.lower()) == remove_diacritics(location_wanted.lower()):

            job_elem = job.find('div', attrs={'class': 'job_header_title'})
            title_element = job_elem.find('h3')
            job_name = title_element.get_text(strip=True)
            print("Job Title: " + job_name)

            job_requirements = job.find('ul', attrs={'class': 'job_requirements'})
            company_element = job_requirements.find('strong')
            company_name = company_element.next_sibling.strip()
            print("Company Name: " + company_name)


            print("Location: " + location)
            print("Post-Date: " + post_date)

            job_tags_elem = job.find('ul', attrs={'class': 'job_tags'})
            job_tags = job_tags_elem.find_all('li')
            print("Job Tags: ", end='')
            index = 1
            for job_tag in job_tags:
                job_tag_elem = job_tag.find('a')
                job_tag_name = job_tag_elem.get_text(strip=True)
                if index == len(job_tags):
                    print(job_tag_name + " ", end='')
                else:
                    print(job_tag_name + ", ", end='')
                index += 1

            print('\n')
            cnt += 1
            if cnt == 7:
                break


if __name__ == '__main__':
   if len(sys.argv) < 2:
       print("Usage: python job_search.py <language> <location_wanted>")
       exit(1)
   if len(sys.argv) == 2:
        language = sys.argv[1]
        location_wanted = None
   elif len(sys.argv) == 3:
       language = sys.argv[1]
       location_wanted = sys.argv[2]

   find_jobs(language, location_wanted)