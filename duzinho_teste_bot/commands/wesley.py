"""Command wesley."""
import random

from . import CallbackContext, Update


def wesley(update: Update, context: CallbackContext):  # nosec
    """Return message for wesley command."""
    mylist = [
        'Wesley lindinho da mamae',
        'ueslinho o guerreiro',
        'ueslinho morre toda hora no valoras',
    ]
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=random.choice(mylist)
    )
