"""Test echo method."""
from telegram import Update
from telegram.ext import CallbackContext


def echo(update: Update, context: CallbackContext):
    """Echo command."""
    print(update.effective_chat.id)
    text = f'Falou: {update.message.text}?'
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
