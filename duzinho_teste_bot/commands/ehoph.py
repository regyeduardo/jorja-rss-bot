"""Command ehoph."""
from telegram import Update
from telegram.ext import CallbackContext


def ehoph(update: Update, context: CallbackContext):
    """Return message for ehoph command."""
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='EhopH E um gostoso pausudo'
    )
