from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
from telegram import ReplyKeyboardMarkup
from utils.parser import *

import logging
import config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('Привет! Я помогу тебе найти нужное слово. Нажми /search, чтобы приступить к поиску')


def help(bot, update):
    update.message.reply_text('Чтобы приступить к поиску слов, нажми/search ')


def echo(bot, update):
    message = update.message.text
    if message == 'По маске':
        update.message.reply_text('Введи слово, в котором пропущенные буквы замени на \'*\'.\nПример: п*ивет')
        search_by_mask(bot, update)
    elif message == 'По описанию':
        update.message.reply_text('Введи задание из кроссворда или его часть.\nПример: рассказ Набокова')
        search_by_description(bot, update)
    else:
        update.message.reply_text(
            'Меня создавали не для общения, а для помощи в поиске слов. Поэтому нажми /search, чтобы я помог тебе')


def search(bot, update):
    keyboard = [['По маске'], ['По описанию']]
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Пожалуйста, выбери как будем искать слово",
                    reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))


def search_by_mask(bot, update):
    word = update.message.text
    update.message.reply_text(get_word_by_mask(word))


def search_by_description(bot, update):
    description = update.message.text
    update.message.reply_text(get_word_by_description(description))


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(config.TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("search", search))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(MessageHandler(Filters.text, search_by_mask))
    dp.add_handler(MessageHandler(Filters.text, search_by_description))
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
