"""Import command."""

from telegram import Update
from telegram.ext import CallbackContext


def importing(update: Update, context: CallbackContext) -> None:
    """Importa feeds de um arquivo OPML..

    Args:
        update (Update): Class from telegram.
        context (CallbackContext): Class from telegram.
    """
    chat_id = str(update.effective_chat.id)
    text = 'Envie um arquivo OPML valido realizar tal acao'
    context.bot.send_message(chat_id, text)
