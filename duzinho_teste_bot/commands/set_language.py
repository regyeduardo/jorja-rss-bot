"""Command set_language."""
from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import CallbackContext

from duzinho_teste_bot.database import SessionLocal, User
from duzinho_teste_bot.utils import flags, get_language_texts


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
    session.close()
    lang = get_language_texts(user.language)(user)

    text = lang.choose_your_language
    languages = [[KeyboardButton(language)] for language in flags]
    context.bot.send_message(
        chat_id,
        text=text,
        reply_markup=ReplyKeyboardMarkup(languages, one_time_keyboard=True),
    )
