"""Bot settings."""
from telegram.ext import (CallbackQueryHandler, CommandHandler, Filters,
                          MessageHandler, Updater)

from . import API_KEY
from .commands import (botao, echo, ehoph, hello, responses, set_timezone,
                       start, wesley)

updater = Updater(token=API_KEY, use_context=True)

dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
hello_handler = CommandHandler('hello', hello)
ehoph_handler = CommandHandler('ehoph', ehoph)
wesley_handler = CommandHandler('wesley', wesley)
settimezone = CommandHandler('set_timezone', set_timezone)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
botao_handler = CommandHandler('botao', botao)
callback = CallbackQueryHandler(responses)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(hello_handler)
dispatcher.add_handler(ehoph_handler)
dispatcher.add_handler(wesley_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(botao_handler)
dispatcher.add_handler(callback)
dispatcher.add_handler(settimezone)
# dispatcher.add_handler(CallbackQueryHandler(callback_query_handler))
