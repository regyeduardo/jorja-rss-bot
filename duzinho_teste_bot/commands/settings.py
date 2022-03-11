"""Settings command."""
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from ..database import SessionLocal, User
from ..utils import get_language_texts


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
    lang = get_language_texts(user.language)(user)
    text = lang.user_data
    context.bot.send_message(chat_id, text, parse_mode=ParseMode.MARKDOWN_V2)
