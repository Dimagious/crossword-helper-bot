import requests
import config
import logging
from bs4 import BeautifulSoup
import lxml

logger = logging.getLogger(__name__)


def get_html(url):
    while True:
        try:
            result = requests.get(url)
            if result.status_code != 200:
                logger.info("Ошибка, Код ответа: %s", result.status_code)
                continue
            logger.info('Удалось подключиться к сайту')
            return result
        except requests.exceptions.RequestException:
            logger.error('Не получилось подключиться к сайту')


def get_description(word):
    if len(word.strip()) == 0:
        logger.error('Пользователь не ввел слово')
        return 'Введите шаблон для поиска'
    else:
        page = get_html(config.URL_FOR_WORD + word)
        description = []
        soup = BeautifulSoup(page, 'lxml')
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
        words = []
        soup = BeautifulSoup(page.content, 'lxml')
        data = soup.find_all('div', class_='wd')
        for item in data:
            w = item.find('a')
            words.append(w.text.strip())
        print('\n'.join(words))
        return '\n'.join(words)


def get_word_by_description(description):
    if len(description.strip()) == 0:
        logger.error('Пользователь не ввел слово')
        return 'Введите шаблон для поиска'
    else:
        page = get_html(config.URL_FOR_DESCRIPTION + description)
        words = []
        soup = BeautifulSoup(page, 'lxml')
        data = soup.find_all('div', class_='wd')
        for item in data:
            w = item.find('a')
            words.append(w.text.strip())
        print('\n'.join(words))
        return '\n'.join(words)


if __name__ == '__main__':
    get_word_by_mask('П**ём')
