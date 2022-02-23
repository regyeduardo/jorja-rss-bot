"""Command start."""
from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    """Return message for start command."""
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='Duzinho bot'
    )
