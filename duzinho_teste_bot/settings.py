"""Bot settings."""
from . import API_KEY
from .commands import (CommandHandler, Filters, MessageHandler, Updater, echo,
                       ehoph, hello, start, wesley)

updater = Updater(token=API_KEY, use_context=True)

dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
hello_handler = CommandHandler('hello', hello)
ehoph_handler = CommandHandler('ehoph', ehoph)
wesley_handler = CommandHandler('wesley', wesley)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(hello_handler)
dispatcher.add_handler(ehoph_handler)
dispatcher.add_handler(wesley_handler)
dispatcher.add_handler(echo_handler)
