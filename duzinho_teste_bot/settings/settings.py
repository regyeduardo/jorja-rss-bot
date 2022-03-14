"""Bot settings."""
from telegram.ext import (CallbackQueryHandler, CommandHandler, Filters,
                          MessageHandler, Updater)

from duzinho_teste_bot import API_KEY
from duzinho_teste_bot.commands import (add, delete, echo, export, feeds,
                                        importing, set_language, set_timezone,
                                        settings, start)
from duzinho_teste_bot.responses import callback_import_command, responses

updater = Updater(token=API_KEY, use_context=True)
dispatcher = updater.dispatcher

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
opml_file_handler = MessageHandler(Filters.document, callback_import_command)
start_handler = CommandHandler('start', start)
set_timezone_handler = CommandHandler('set_timezone', set_timezone)
settings_handler = CommandHandler('settings', settings)
set_language_handler = CommandHandler('set_language', set_language)
add_handler = CommandHandler('add', add)
feeds_handler = CommandHandler('feeds', feeds)
export_handler = CommandHandler('export', export)
import_handler = CommandHandler('import', importing)
delete_handler = CommandHandler('delete', delete)
callback = CallbackQueryHandler(responses)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(set_timezone_handler)
dispatcher.add_handler(set_language_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(feeds_handler)
dispatcher.add_handler(export_handler)
dispatcher.add_handler(import_handler)
dispatcher.add_handler(delete_handler)
dispatcher.add_handler(settings_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(opml_file_handler)
dispatcher.add_handler(callback)
