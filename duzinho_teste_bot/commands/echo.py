"""Test echo method."""
from . import CallbackContext, Update


def echo(update: Update, context: CallbackContext):
    """Echo command."""
    print(update.effective_chat.id)
    text = f'Voce disse: {update.message.text}?'
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
