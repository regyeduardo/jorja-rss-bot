"""Add command."""


import feedparser
from sqlalchemy.exc import IntegrityError
from telegram import Update
from telegram.ext import CallbackContext

from duzinho_teste_bot.database import SessionLocal, User
from duzinho_teste_bot.utils import add_feed, get_language_texts

# import pytz


# https://docs.sqlalchemy.org/en/14/orm/queryguide.html
def add(update: Update, context: CallbackContext):
    """Adiciona novos feeds.

    Args:
        update (Update): Class from telegram
        context (CallbackContext): Class from telegram.
    """
    chat_id = str(update.effective_chat.id)
    session = SessionLocal()
    user = session.query(User).filter(User.id == chat_id).first()
    session.close()
    lang = get_language_texts(user.language)(user)

    if not context.args:
        text = lang.help_add
        context.bot.send_message(chat_id, text)
    else:
        feed = context.args[0]

        try:
            request = feedparser.parse(feed)

            if request.bozo:
                text = lang.invalid_feed
                context.bot.send_message(chat_id, text)
            else:
                add_feed(request, chat_id)
                text = lang.default_successful_updated
                context.bot.send_message(chat_id, text)

        except IntegrityError:
            text = lang.has_feed
            context.bot.send_message(chat_id, text)
