"""Command start."""
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from ..database.db import SessionLocal
from ..database.models.users import User
# from ..utils.gmt import return_gmt_buttons
from ..utils.language import get_default_error_message, get_user_data


def start(update: Update, context: CallbackContext):
    """Return message for start command."""
    session = SessionLocal()
    # print(context)
    chat_id = str(update.effective_chat.id)
    user = session.query(User).filter(User.id == chat_id).first()

    if not user:
        user = User()
        user.id = chat_id
        user_language = update.effective_user.language_code

        if user_language in ['es', 'pt-br']:
            user.language = user_language
        else:
            user.language = 'en'

        user.timezone = 'Europe/London'

        try:
            session.add(user)
            session.commit()

            text = get_user_data(user.timezone, user.language)
            context.bot.send_message(
                chat_id, text, parse_mode=ParseMode.MARKDOWN_V2
            )
        except:   # pylint: disable=bare-except
            text = get_default_error_message(user.languege)
            context.bot.send_message(chat_id, text)

    text = get_user_data(user.timezone, user.language)
    context.bot.send_message(chat_id, text, parse_mode=ParseMode.MARKDOWN_V2)
    # return_gmt_buttons(chat_id=chat_id)
    # update.effective_message.delete()
