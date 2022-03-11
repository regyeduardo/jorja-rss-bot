"""Feeds command."""
from telegram import Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext

from duzinho_teste_bot.database import SessionLocal, Subscription, User
from duzinho_teste_bot.utils import get_language_texts


def feeds(update: Update, context: CallbackContext):
    """Mostra ao usuários todos os seus feeds cadastrados.

    Args:
        update (Update): Class from telegram.
        context (CallbackContext): Class from telegram.
    """
    chat_id = str(update.effective_chat.id)
    session = SessionLocal()
    user = session.query(User).filter(User.id == chat_id).first()
    lang = get_language_texts(user.language)(user)
    subs = (
        session.query(Subscription)
        .filter(Subscription.user_id == chat_id)
        .all()
    )
    session.close()
    text = ''
    for sub in subs:
        added = sub.created_at.astimezone(user.timezone).strftime(
            '%d %b %H:%M %z'
        )
        text += f'{added} {sub.url}\n'

    try:
        context.bot.send_message(chat_id, text)
    except BadRequest:
        text = lang.no_feeds
        context.bot.send_message(chat_id, text)
