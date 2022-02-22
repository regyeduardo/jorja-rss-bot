"""Bot settings."""
# API_KEY = config('TELEGRAM_API_KEY')
from . import API_KEY
from .commands import CommandHandler, Updater, ehoph, hello, start, wesley

# from decouple import config


updater = Updater(token=API_KEY, use_context=True)

dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
hello_handler = CommandHandler('hello', hello)
ehoph_handler = CommandHandler('ehoph', ehoph)
wesley_handler = CommandHandler('wesley', wesley)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(hello_handler)
dispatcher.add_handler(ehoph_handler)
dispatcher.add_handler(wesley_handler)
