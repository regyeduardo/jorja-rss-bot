"""Command set_timezone."""
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from ..utils.gmt import return_gmt_buttons


def set_timezone(update: Update, context: CallbackContext):
    """Return message for ehoph command."""
    # https://telegra.ph/Available-timezones-02-23
    print(context)
    id = update.effective_chat.id
    return_gmt_buttons(chat_id=id)
    update.effective_message.delete()
