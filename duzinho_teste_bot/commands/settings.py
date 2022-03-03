"""Settings command."""
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from ..database.db import SessionLocal
from ..database.models.users import User
from ..utils.language import get_user_data


def settings(update: Update, context: CallbackContext) -> None:
    """
    Retorna os dados do usuario.

    Args:
        update -- Tipo Update do pacote telegram.
        context -- Tipo CallbackContext do pacote telegram.ext.
    """
    chat_id = str(update.effective_chat.id)
    session = SessionLocal()
    user = session.query(User).filter(User.id == chat_id).first()

    text = get_user_data(user.timezone, user.language)
    context.bot.send_message(chat_id, text, parse_mode=ParseMode.MARKDOWN_V2)
