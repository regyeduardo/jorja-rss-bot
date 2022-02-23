"""Command hello."""
from telegram import Update
from telegram.ext import CallbackContext


def hello(update: Update, context: CallbackContext):
    """Return message for hello command."""
    print(update.effective_chat.id)
    print(context.args)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='Hello World'
    )
