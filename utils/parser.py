from bs4 import BeautifulSoup
from utils import messages
import requests
import config
import logging
import re

logger = logging.getLogger(__name__)


def get_word(user_input):
    if len(user_input.strip()) == 0:
        logger.error(messages.NO_INPUT)
        return messages.INPUT_PLEASE
    elif not re.search('[*]', user_input):
        logger.info(messages.SEARCHING_BY_DESCRIPTION)
        page = get_html(config.URL_FOR_DESCRIPTION + user_input)
    else:
        logger.info(messages.SEARCHING_BY_MASK)
        page = get_html(config.URL_FOR_WORD + user_input + '&def=')
    words = []
    soup = BeautifulSoup(page.content, 'lxml')
    data = soup.find_all('div', class_='wd')
    for item in data:
        w = item.find('a')
        words.append(w.text.strip())
    print('\n'.join(words))
    return '\n'.join(words) if words else messages.NO_RESULT_AFTER_SEARCH


def get_html(url):
    while True:
        try:
            result = requests.get(url)
            if result.status_code != 200:
                logger.info(messages.STATUS_CODE_ERROR, result.status_code)
                continue
            logger.info(messages.SUCCESS_CONNECTION)
            return result
        except requests.exceptions.RequestException:
            logger.error(messages.FAILED_CONNECTION)
