"""Command hello."""
from . import CallbackContext, Update


def hello(update: Update, context: CallbackContext):
    """Return message for hello command."""
    print(context._user_id_and_data)  # pylint: disable=W0212
    print(context.args)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='Hello World'
    )
