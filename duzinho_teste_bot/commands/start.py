"""Command start."""
from . import CallbackContext, Update


def start(update: Update, context: CallbackContext):
    """Return message for start command."""
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='Duzinho bot'
    )
