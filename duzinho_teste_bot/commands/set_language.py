"""Command set_language."""
from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import CallbackContext

from ..database.db import SessionLocal
from ..database.models.users import User
from ..utils import flags
from ..utils.language import choose_your_language


def set_language(update: Update, context: CallbackContext) -> None:
    """
    Atualiza o linguagem do usuario.

    Args:
        update -- Tipo Update do pacote telegram.
        context -- Tipo CallbackContext do pacote telegram.ext.
    """
    chat_id = str(update.effective_chat.id)
    session = SessionLocal()
    user = session.query(User).filter(User.id == chat_id).first()

    text = choose_your_language(user.language)
    languages = [[KeyboardButton(language)] for language in flags]
    context.bot.send_message(
        chat_id,
        text=text,
        reply_markup=ReplyKeyboardMarkup(languages, one_time_keyboard=True),
    )
