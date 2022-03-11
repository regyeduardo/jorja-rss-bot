"""Command start."""
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from ..database import SessionLocal, User
from ..utils import get_language_texts


def start(update: Update, context: CallbackContext):
    """Return message for start command."""
    session = SessionLocal()
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
        lang = get_language_texts(user.language)(user)

        try:
            session.add(user)
            session.commit()
            text = lang.user_data

            context.bot.send_message(
                chat_id, text, parse_mode=ParseMode.MARKDOWN_V2
            )
        except:   # pylint: disable=bare-except
            text = lang.default_error
            context.bot.send_message(chat_id, text)
    else:
        lang = get_language_texts(user.language)(user)
        text = lang.user_data
        context.bot.send_message(
            chat_id, text, parse_mode=ParseMode.MARKDOWN_V2
        )
