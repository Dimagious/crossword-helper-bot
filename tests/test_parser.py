from utils.parser import *
import unittest


class TestParser(unittest.TestCase):
    def test_get_html(self):
        self.assertEquals(get_html('https://www.yandex.ru/').startswith('<'), True)
        self.assertEquals(get_html('https://www.yandex.ru/').endswith('>'), True)
        self.assertEquals(get_html('www.dfvsduvfjpwofivpwueufv.ru'), '')

    def test_get_description(self):
        self.assertEquals(get_description('экзистенция')[2], 'существование')
        self.assertEquals(get_description(''), 'Введите шаблон для поиска')
        self.assertEquals(get_description('        '), 'Введите шаблон для поиска')

    def test_get_word_by_mask(self):
        self.assertEquals(get_word_by_mask('электр*чество')[0], 'электричество')
        self.assertEquals(get_word_by_mask(''), 'Введите шаблон для поиска')
        self.assertEquals(get_word_by_mask('  '), 'Введите шаблон для поиска')

    def test_get_word_by_description(self):
        self.assertEquals(get_word_by_description('существование')[3], 'акклиматизирование')
        self.assertEquals(get_word_by_description(''), 'Введите шаблон для поиска')
        self.assertEquals(get_word_by_description('    '), 'Введите шаблон для поиска')