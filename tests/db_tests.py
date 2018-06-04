import unittest

from database.db import Words


class MyTest(unittest.TestCase):
    def test_check_word(self):
        self.assertIs(Words.check_word('электричество'), True, 'DB has not this word')
        self.assertIsNot(Words.check_word('провода'), True, 'DB has this word')

    def test_word_by_id(self):
        self.assertEquals(Words.word_by_id(2), 'полемика', 'DB has not word with this id')
        self.assertNotEquals(Words.word_by_id(2), 'дом', 'DB has word with this id')

    # TODO
    def test_description_by_word(self):
        self.assertEquals(Words.description_by_word('полемика'),
                          'спор при обсуждении;спор, обсуждение проблем, вопросов;спор при обсуждении проблем',
                          'DB has not word with this description')
        self.assertNotEquals(Words.description_by_word('полемика'), 'дом', 'DB has word with this description')
