""" "Delete command."""


from sqlalchemy.orm.exc import UnmappedInstanceError
from telegram import Update
from telegram.ext import CallbackContext

from duzinho_teste_bot.database import SessionLocal, Subscription, User
from duzinho_teste_bot.utils import get_language_texts


def delete(update: Update, context: CallbackContext) -> None:
    """Deleta um feed da lista do usuário.

    Args:
        update (Update): Class from telegram.
        context (CallbackContext): Class from telegram.
    """
    chat_id = str(update.effective_chat.id)
    session = SessionLocal()
    user = session.query(User).filter(User.id == chat_id).first()
    session.close()
    lang = get_language_texts(user.language)(user)
    if not context.args:
        text = lang.help_delete
        context.bot.send_message(chat_id, text)
    else:
        feed_url = context.args[0]

        try:
            session = SessionLocal()
            sub = (
                session.query(Subscription)
                .filter(Subscription.user_id == chat_id)
                .filter(Subscription.url == feed_url)
                .first()
            )
            session.delete(sub)
            session.commit()
            session.close()
            text = lang.default_successful_updated
            context.bot.send_message(chat_id, text)
        except UnmappedInstanceError:
            text = lang.cannot_delete
            context.bot.send_message(chat_id, text)
