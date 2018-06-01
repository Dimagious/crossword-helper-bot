from pony.orm import *
import re
import config
import unittest

db = Database()


class Words(db.Entity):
    id = PrimaryKey(int)
    word = Required(str)
    description = Required(str)

    # поиск слов по id
    @classmethod
    @db_session
    def word_by_id(cls, id):
        return get(w.word for w in Words if w.id == id)

    # поиск слов по описанию
    @classmethod
    @db_session
    def description_by_word(cls, word):
        return get(w.description for w in Words if w.id == word.id)

    # поиск слова по маске
    @classmethod
    @db_session
    def check_word(cls, word):
        return Words.exists(word=word)


db.bind(provider='postgres', user=config.USER, password=config.PASSWORD,
        host=config.HOST, database=config.DATABASE)
db.generate_mapping(create_tables=True)
