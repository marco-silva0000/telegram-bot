import os
import telegram
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
load_dotenv()

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.DEBUG)

bot = telegram.Bot(token=os.getenv("BOT_TOKEN"))
print(bot.get_me())

updater = Updater(os.getenv("BOT_TOKEN"))

def echo(bot, update, args):
    args = "".join(args)
    update.message.reply_text(f"user said:{args}")

def start(bot, update, *args, **kwargs):
    print(bot)
    print(update)
    print(args)
    print(kwargs)
    update.message.reply_text("I'm a bot, please talk to me!")


def bear(bot, update):
    from image_search import bear_search
    update.message.reply_text(bear_search())

start_handler = CommandHandler('start', start)
bear_handler = CommandHandler(['bear', 'urso', '🐻', '🧸', '🐨'], bear)
updater.dispatcher.add_handler(CommandHandler("test", echo, pass_args=True))
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(bear_handler)


updater.start_polling()

