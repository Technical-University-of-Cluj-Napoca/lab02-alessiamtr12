import sys

from bs4 import BeautifulSoup
import requests


def define(word: str) -> None:
    url = "https://dexonline.ro/definitie/" + word
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    definition = soup.find("span", attrs={"class": "tree-def html"})
    print(definition.text)

if __name__ == '__main__':
    word = sys.argv[1]
    define(word)
