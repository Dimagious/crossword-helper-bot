import requests
import config
import logging
import re
from bs4 import BeautifulSoup

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


def get_word(user_input):
    if len(user_input.strip()) == 0:
        logger.error('Пользователь не ввел слово')
        return 'Введите шаблон для поиска'
    elif not re.search('[*]', user_input):
        logger.info('Выполняется поиск по описанию')
        page = get_html(config.URL_FOR_DESCRIPTION + user_input)
    else:
        logger.info('Выполняется поиск по маске')
        page = get_html(config.URL_FOR_WORD + user_input + '&def=')
    words = []
    soup = BeautifulSoup(page.content, 'lxml')
    data = soup.find_all('div', class_='wd')
    for item in data:
        w = item.find('a')
        words.append(w.text.strip())
    print('\n'.join(words))
    return '\n'.join(words)


if __name__ == '__main__':
    get_word_by_mask('Наб**ов')
