"""Bot settings."""
from telegram.ext import (CallbackQueryHandler, CommandHandler, Filters,
                          MessageHandler, Updater)

from .. import API_KEY
from ..commands import (add, delete, echo, feeds, set_language, set_timezone,
                        settings, start)
from ..responses import responses

updater = Updater(token=API_KEY, use_context=True)
dispatcher = updater.dispatcher

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
start_handler = CommandHandler('start', start)
set_timezone_handler = CommandHandler('set_timezone', set_timezone)
settings_handler = CommandHandler('settings', settings)
set_language_handler = CommandHandler('set_language', set_language)
add_handler = CommandHandler('add', add)
feeds_handler = CommandHandler('feeds', feeds)
delete_handler = CommandHandler('delete', delete)
callback = CallbackQueryHandler(responses)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(set_timezone_handler)
dispatcher.add_handler(set_language_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(feeds_handler)
dispatcher.add_handler(delete_handler)
dispatcher.add_handler(settings_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(callback)
