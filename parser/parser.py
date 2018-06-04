import requests
import config
import logging
from bs4 import BeautifulSoup
logger = logging.getLogger(__name__)


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except requests.exceptions.RequestException:
        logger.error('Не получилось подключиться к сайту')
        return ''


def get_description(word):
    page = get_html(config.URL_FOR_WORD + word + '&def=')
    description = []
    soup = BeautifulSoup(page, 'html.parser')
    data = soup.find('div', class_='wd st')
    for desc in data.find_all('p'):
        description.append(desc.text.strip())
    print(description)
    return description


def get_word(description):
    page = get_html(config.URL_FOR_DESCRIPTION + description)
    word = []
    soup = BeautifulSoup(page, 'html.parser')
    data = soup.find('div', class_='wd st')
    for w in data.find_all('a'):
        word.append(w.text.strip())
    print(word[0])
    return word[0]


if __name__ == "__main__":
    get_description('стол')
    get_word('четыре братца под')
