from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
import logging

# Enable logging
import config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Привет! Я помогу тебе найти нужное слово. Нажми /search, чтобы приступить к поиску')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Чтобы приступить к поиску слов, нажми/search ')


def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(
        'Меня создавали не для общения, а для помощи в поиске слов. Поэтому нажми /search, чтобы я помог тебе')


def search(bot, update, args):
    """Searches the words, that user wants"""
    keyboard = [['По маске'], ['По описанию']]
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Пожалуйста, выбери как будем искать слово",
                    reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(config.TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("search", search))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()