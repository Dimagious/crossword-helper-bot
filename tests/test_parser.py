from parser import *
import config
import unittest


class TestParser(unittest.TestCase):
    def test_get_html(self):
        self.assertEqual(get_html(config.TEST_URL).status_code, 200)

    def test_get_word_by_mask(self):
        self.assertEqual(get_word('электр*чество'), 'электричество')
        self.assertEqual(get_word(''), messages.INPUT_PLEASE)
        self.assertEqual(get_word('  '), messages.INPUT_PLEASE)

    def test_get_word_by_description(self):
        self.assertEqual(get_word('Азкабан'), 'дементор')
        self.assertEqual(get_word('плащ Аббата'), messages.NO_RESULT_AFTER_SEARCH)
        self.assertEqual(get_word(''), messages.INPUT_PLEASE)
        self.assertEqual(get_word('    '), messages.INPUT_PLEASE)
