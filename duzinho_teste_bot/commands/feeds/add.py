"""Add command."""

from datetime import datetime
from time import mktime

import feedparser
from telegram import Update
from telegram.ext import CallbackContext

from duzinho_teste_bot.database import SessionLocal, Subscription, User
from duzinho_teste_bot.utils import get_language_texts

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
        has_feed = (
            session.query(Subscription)
            .filter(Subscription.user_id == chat_id)
            .filter(Subscription.url == feed)
            .scalar()
        )

        if has_feed:
            text = lang.has_feed
            context.bot.send_message(chat_id, text)
        else:
            request = feedparser.parse(feed)

            if request.bozo:
                text = lang.invalid_feed
                context.bot.send_message(chat_id, text)
            else:
                subs = Subscription()
                subs.url = feed
                subs.user_id = chat_id

                try:
                    last_post = datetime.strptime(
                        request.entries[0].published,
                        '%a, %d %b %Y %H:%M:%S %z',
                    )
                    subs.datetime_last_post = last_post
                except ValueError:
                    parsed = request.entries[0].published_parsed
                    last_post = datetime.fromtimestamp(mktime(parsed))

                    # if not last_post.tzinfo:
                    #     timezone = pytz.timezone('GMT')
                    #     last_post = timezone.localize(last_post)

                    subs.datetime_last_post = last_post

                session = SessionLocal()
                session.add(subs)
                session.commit()
                session.close()
                text = lang.default_successful_updated
                context.bot.send_message(chat_id, text)
