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
    if len(word.strip()) == 0:
        logger.error('Пользователь не ввел слово')
        return 'Введите шаблон для поиска'
    else:
        page = get_html(config.URL_FOR_WORD + word)
        description = []
        soup = BeautifulSoup(page, 'html.parser')
        data = soup.find('div', class_='wd st')
        for desc in data.find_all('p'):
            description.append(desc.text.strip())
        print(description)
        return description


def get_word_by_mask(mask):
    if len(mask.strip()) == 0:
        logger.error('Пользователь не ввел слово')
        return 'Введите шаблон для поиска'
    else:
        page = get_html(config.URL_FOR_WORD + mask + '&def=')
        word = []
        soup = BeautifulSoup(page, 'html.parser')
        data = soup.find_all('div', class_='wd')
        for item in data:
            w = item.find('a')
            word.append(w.text.strip())
        print(word)
        return word


def get_word_by_description(description):
    if len(description.strip()) == 0:
        logger.error('Пользователь не ввел слово')
        return 'Введите шаблон для поиска'
    else:
        page = get_html(config.URL_FOR_DESCRIPTION + description)
        word = []
        soup = BeautifulSoup(page, 'html.parser')
        data = soup.find_all('div', class_='wd')
        for item in data:
            w = item.find('a')
            word.append(w.text.strip())
        print(word)
        return word
