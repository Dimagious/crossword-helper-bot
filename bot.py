# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup
from utils.parser import *
import logging
import config

TYPE, TEXT = range(2)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def help(bot, update):
    update.message.reply_text('Привет! Я помогу тебе найти нужное слово. Нажми /search, чтобы приступить к поиску')


def choose(bot, update):
    if update.message.text == 'По маске':
        update.message.reply_text('Введи слово, в котором пропущенные буквы замени на \'*\'.\nПример: п*ивет')
        return TEXT
    elif update.message.text == 'По описанию':
        update.message.reply_text('Введи задание из кроссворда или его часть.\nПример: рассказ Набокова')
        return TEXT
    else:
        update.message.reply_text(
            'Меня создавали исключительно для помощи в поиске слов. '
            'Поэтому нажми /start и выбери как будем искать слово')
        return ConversationHandler.END


def start(bot, update):
    keyboard = [['По маске'], ['По описанию']]
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Пожалуйста, выбери как будем искать слово",
                    reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
    return TYPE


def search(bot, update):
    search_by_mask(bot, update)
    return ConversationHandler.END


def search_by_mask(bot, update):
    word = update.message.text
    update.message.reply_text(get_word_by_mask(word))
    update.message.reply_text('Если буду нужен ещё жми /start')


def search_by_description(bot, update):
    description = update.message.text
    update.message.reply_text(get_word_by_description(description))
    update.message.reply_text('Если буду нужен ещё жми /start')


def cancel(bot, update):
    bot.sendMessage(update.message.chat_id, "Bye!")
    return ConversationHandler.END


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    updater = Updater(config.TOKEN)
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            TYPE: [MessageHandler(Filters.text, choose)],
            TEXT: [MessageHandler(Filters.text, search)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )
    dp.add_handler(conv_handler)

    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, search_by_mask))
    dp.add_handler(MessageHandler(Filters.text, search_by_description))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
