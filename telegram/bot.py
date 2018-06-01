import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help'])
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
    bot.send_message(message.chat.id, "Как будем искать слово?", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(message):
    pass


if __name__ == '__main__':
    bot.polling(none_stop=True)
