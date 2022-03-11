"""Tasks module."""
import asyncio
from datetime import datetime
from time import mktime

import feedparser
import pytz
from telegram import ParseMode
from sqlalchemy.exc import TimeoutError

from duzinho_teste_bot import bot
from duzinho_teste_bot.database import SessionLocal, Subscription, User, engine


async def get_feeds():
    """Obtem todos os feeds de todos os usuarios."""
    # pylint: disable=R0914
    while True:
        session = SessionLocal()
        users = session.query(User).all()
        session.close()

        if users:
            for user in users:
                session = SessionLocal()
                subs = (
                    session.query(Subscription)
                    .filter(Subscription.user_id == user.id)
                    .all()
                )
                session.close()

                if subs:
                    check_subs(subs, user)

        await asyncio.sleep(60)


def check_subs(subs, user):
    """Checa novos posts de cada feed e caso houver
    manda os posts novos.

    Args:
        subs (Subscription): Todos os feeds do usuario.
        user (User): Usuario atual..
    """
    try:
        for sub in subs:
            sub_last_post = sub.datetime_last_post

            feed = feedparser.parse(sub.url)

            if feed.bozo:
                bot.send_message(user.id, f'Feed {sub.url} inválido')
            else:
                parsed = feed.entries[0].published_parsed
                feed_last_post = datetime.fromtimestamp(mktime(parsed))

                if sub_last_post < feed_last_post:
                    sub.datetime_last_post = feed_last_post
                    session = SessionLocal()
                    session.add(sub)
                    session.commit()
                    session.close()

                    timezone = pytz.timezone(str(user.timezone))

                    for post in feed.entries:

                        post_published = datetime.fromtimestamp(
                            mktime(post.published_parsed)
                        )

                        if sub_last_post < post_published:
                            post_pulished_gmt = pytz.timezone('GMT').localize(
                                post_published
                            )

                            title = post['title']
                            url_link = post['link']
                            date_converted = datetime.strftime(
                                post_pulished_gmt.astimezone(timezone),
                                '%Y %b %d %H:%M:%S %z',
                            )

                            text = (
                                f'*{title}*'
                                f'\n[Post completo]({url_link})'
                                f'\nPublicado em: _{date_converted}_'
                            )

                            special = [
                                '~',
                                '`',
                                '>',
                                '+',
                                '-',
                                '=',
                                '|',
                                '{',
                                '}',
                                '.',
                                '!',
                            ]
                            # '[', ']', '(', ')', '*', '#', '_'
                            formated_text = ''
                            for char in text:
                                if char in special:
                                    formated_text += f'\\{char}'
                                else:
                                    formated_text += f'{char}'

                            bot.send_message(
                                user.id,
                                formated_text,
                                parse_mode=ParseMode.MARKDOWN_V2,
                            )
    except TimeoutError:
        engine.dispose()