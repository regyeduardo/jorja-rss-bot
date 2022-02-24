"""Command start."""
from telegram import Update
from telegram.ext import CallbackContext

from ..utils.gmt import return_gmt_buttons


def start(update: Update, context: CallbackContext):
    """Return message for start command."""
    print(context)
    # pylint: disable-next=invalid-name, redefined-builtin
    id = update.effective_chat.id
    return_gmt_buttons(chat_id=id)
    update.effective_message.delete()
