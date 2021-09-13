import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = '1974728241:AAHeUTVr4mjmdQXQbMWTfG0LmV5PBKT8lmQ'


def start(update, context):
    print(update)
    author = update.message.chat.first_name
    reply = 'Hi ! {}'.format(author)
    context.bot.send_message(chat_id=update.message.chat_id, text=reply)


def _help(update, context):
    help_text = 'Hey! This is a help text.'
    context.bot.send_message(chat_id=update.message.chat_id, text=help_text)


def echo_text(update, context):
    context.bot.send_message(
        chat_id=update.message.chat_id, text=update.message.text)


def echo_sticker(update, context):
    context.bot.send_sticker(chat_id=update.message.chat_id,
                             sticker=update.message.sticker.file_id)


def error(update, context):
    logger.error("Update '%s' caused error '%s'", update, context.error)


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", _help))
    dp.add_handler(MessageHandler(Filters.text, echo_text))
    dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
    dp.add_error_handler(error)

    updater.start_polling()
    logger.info('Started polling...')
    updater.idle()


if __name__ == '__main__':
    main()
