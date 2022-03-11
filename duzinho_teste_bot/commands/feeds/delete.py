""" "Delete command."""


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

        session = SessionLocal()

        feed = context.args[0]

        has_feed = (
            session.query(Subscription)
            .filter(Subscription.user_id == chat_id)
            .filter(Subscription.url == feed)
            .scalar()
        )
        session.close()

        if has_feed:
            session = SessionLocal()
            subs = (
                session.query(Subscription)
                .filter(Subscription.user_id == chat_id)
                .filter(Subscription.url == feed)
                .first()
            )
            try:
                text = lang.default_successful_updated
                session.delete(subs)
                session.commit()
                session.close()
                context.bot.send_message(chat_id, text)
            except:  # pylint: disable = bare-except
                text = lang.default_error
                context.bot.send_message(chat_id, text)
                session.close()
        else:
            session.close()
            text = lang.cannot_delete
            context.bot.send_message(chat_id, text)
