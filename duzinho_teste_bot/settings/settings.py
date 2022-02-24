"""Bot settings."""
from telegram.ext import (CallbackQueryHandler, CommandHandler, Filters,
                          MessageHandler, Updater)

from .. import API_KEY
from ..commands import echo, set_timezone, start
from ..responses import responses

updater = Updater(token=API_KEY, use_context=True)
dispatcher = updater.dispatcher

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
start_handler = CommandHandler('start', start)
set_timezone_handler = CommandHandler('set_timezone', set_timezone)
callback = CallbackQueryHandler(responses)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(set_timezone_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(callback)
