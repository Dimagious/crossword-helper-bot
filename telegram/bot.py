from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
import logging
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


def search(bot, update):
    keyboard = [['/шаблон'], ['/описание']]
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Пожалуйста, выбери как будем искать слово",
                    reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))


def search_by_mask(bot, update):
    update.message.reply_text('здесь будут найденные слова')
    # bot.sendMessage(update.message.chat_id, get_description(update.message.text))


def search_by_description(bot, update):
    update.message.reply_text('здесь будут найденные слова')
    # bot.sendMessage(update.message.chat_id, get_word(update.message.text))


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
    dp.add_handler(CommandHandler("шаблон", search_by_mask))
    dp.add_handler(CommandHandler("описание", search_by_description))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
