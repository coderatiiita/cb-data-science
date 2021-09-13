import logging
from flask import Flask, request
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
from telegram import Bot, Update

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = '1974728241:AAHeUTVr4mjmdQXQbMWTfG0LmV5PBKT8lmQ'

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello!'


@app.route(f'/{TOKEN}', methods={'GET', 'POST'})
def webhook():
    update = Update.de_json(request.get_json(), bot)

    dp.process_update(update)
    return 'ok'


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


if __name__ == '__main__':
    bot = Bot(TOKEN)
    bot.set_webhook('https://664a-103-92-42-107.ngrok.io/' + TOKEN)
    dp = Dispatcher(bot, None)

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", _help))
    dp.add_handler(MessageHandler(Filters.text, echo_text))
    dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
    dp.add_error_handler(error)

    app.run(port=8443)
