# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram import ReplyKeyboardMarkup
from utils.parser import *
import logging
import config

TYPE, TEXT = range(2)
logging.basicConfig(format=messages.LOGGING, level=logging.INFO)
logger = logging.getLogger(__name__)


def help(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=messages.HELP)


def choose(bot, update):
    if update.message.text == messages.BY_MASK:
        bot.sendMessage(chat_id=update.message.chat_id, text=messages.MASK_EXAMPLE)
        return TEXT
    elif update.message.text == messages.BY_DESCRIPTION:
        bot.sendMessage(chat_id=update.message.chat_id, text=messages.DESCRIPTION_EXAMPLE)
        return TEXT
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text=messages.IF_NOTHING_CHOSEN)
        return ConversationHandler.END


def start(bot, update):
    keyboard = [[messages.BY_MASK], [messages.BY_DESCRIPTION]]
    bot.sendMessage(chat_id=update.message.chat_id,
                    text=messages.CHOOSE,
                    reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
    return TYPE


def search(bot, update):
    search_by_mask(bot, update)
    return ConversationHandler.END


def search_by_mask(bot, update):
    word = update.message.text
    bot.sendMessage(chat_id=update.message.chat_id, text=get_word(word))
    bot.sendMessage(chat_id=update.message.chat_id, text=messages.TRY_AGAIN)


def search_by_description(bot, update):
    description = update.message.text
    bot.sendMessage(chat_id=update.message.chat_id, text=get_word(description))
    bot.sendMessage(chat_id=update.message.chat_id, text=messages.TRY_AGAIN)


def cancel(bot, update):
    bot.sendMessage(update.message.chat_id, messages.BYE)
    return ConversationHandler.END


def error(bot, update, error):
    logger.warning(messages.ERROR_LOGGING, update, error)


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
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

