import telebot
from telebot import types
import config
from database.db import *

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hello)


def hello(message):
    bot.send_message(
        message.chat.id,
        'Привет, {name}. Рад тебя видеть.'.format(name=message.text))
    markup = types.ReplyKeyboardMarkup(row_width=2)
    mask_btn = types.KeyboardButton('По маске')
    desc_btn = types.KeyboardButton('По описанию')
    markup.add(mask_btn, desc_btn)
    bot.send_message(message.chat.id, "Пожалуйста выбери как будем искать слово", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def repeater(message):
    if message == 'По маске':
        sent = bot.send_message(message.chat.id, 'Введи своё слово в соответствии с шаблоном: пр*в*т')
        bot.register_next_step_handler(sent, search_by_word)
    elif message == 'По описанию':
        sent = bot.send_message(message.chat.id, 'Введи задание из кроссворда')
        bot.register_next_step_handler(sent, search_by_description)
    else:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        mask_btn = types.KeyboardButton('По маске')
        desc_btn = types.KeyboardButton('По описанию')
        markup.add(mask_btn, desc_btn)
        bot.send_message(message.chat.id, "Пожалуйста выбери как будем искать слово", reply_markup=markup)


@bot.message_handler(commands=['by_word'], content_types=["text"])
def search_by_word(message):
    bot.send_message(message.chat.id, 'Скоро тут будет поиск по маске')


@bot.message_handler(commands=['by_description'], content_types=["text"])
def search_by_description(message):
    bot.send_message(message.chat.id, 'Скоро тут будет поиск по маске')


@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(message):
    pass


if __name__ == '__main__':
    bot.polling(none_stop=True)
