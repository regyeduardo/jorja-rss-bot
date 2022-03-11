"""Command set_timezone."""
import pytz
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from ..database import SessionLocal, User
from ..utils import get_language_texts


def set_timezone(update: Update, context: CallbackContext) -> None:
    """
    Atualiza o fuso-horario do usuario.

    Args:
        update (Update) -- Tipo Update do pacote telegram.
        context (CallbackContext) -- Tipo CallbackContext do pacote telegram.ext.
    """
    chat_id = str(update.effective_chat.id)
    session = SessionLocal()
    user = session.query(User).filter(User.id == chat_id).first()
    lang = get_language_texts(user.language)(user)

    if not context.args:
        text = lang.help_set_timezone
        context.bot.send_message(
            chat_id, text, parse_mode=ParseMode.MARKDOWN_V2
        )
    elif context.args[0] in pytz.common_timezones:
        timezone = pytz.timezone(context.args[0])
        user.timezone = timezone

        try:
            session.add(user)
            session.commit()
            text = lang.default_successful_updated
            context.bot.send_message(chat_id, text)
        except:  # pylint: disable=bare-except
            text = lang.default_error
            context.bot.send_message(chat_id, text)
    else:
        text = lang.default_error
        context.bot.send_message(chat_id, text)
