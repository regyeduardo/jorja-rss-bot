"""Command set_timezone."""
import pytz
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from ..database.db import SessionLocal
from ..database.models.users import User
from ..utils.language import (get_default_error_message,
                              get_help_set_timezone_command,
                              get_successful_update)

# def set_timezone(update: Update, context: CallbackContext):
#     """Return message for set_timezone command."""
#     print(context)
#     chat_id = update.effective_chat.id
#     return_gmt_buttons(chat_id=chat_id)
#     update.effective_message.delete()


def set_timezone(update: Update, context: CallbackContext) -> None:
    """
    Atualiza o fuso-horario do usuario.

    Args:
        update -- Tipo Update do pacote telegram.
        context -- Tipo CallbackContext do pacote telegram.ext.
    """
    chat_id = str(update.effective_chat.id)
    session = SessionLocal()
    user = session.query(User).filter(User.id == chat_id).first()

    if not context.args:
        text = get_help_set_timezone_command(user.language)
        context.bot.send_message(
            chat_id, text, parse_mode=ParseMode.MARKDOWN_V2
        )
    elif context.args[0] in pytz.common_timezones:
        timezone = pytz.timezone(context.args[0])
        user.timezone = timezone

        try:
            session.add(user)
            session.commit()
            text = get_successful_update(user.language)
            context.bot.send_message(chat_id, text)
        except:  # pylint: disable=bare-except
            text = get_default_error_message(user.language)
            context.bot.send_message(chat_id, text)
    else:
        text = get_default_error_message(user.language)
        context.bot.send_message(chat_id, text)
