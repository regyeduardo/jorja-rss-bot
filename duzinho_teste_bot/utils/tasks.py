"""Tasks module."""
import asyncio
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
# from email.MIMEImage import MIMEImage
from email.mime.text import MIMEText
from time import mktime

import feedparser
import pytz
from decouple import config
from telegram import ParseMode
from telegram.error import BadRequest

from duzinho_teste_bot import bot
from duzinho_teste_bot.database import SessionLocal, Subscription, User

# from sqlalchemy.exc import TimeoutError


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
                            f'*{parse_md(title)}*'
                            f'\n[Post completo]({parse_md(url_link)})'
                            f'\nPublicado em: _{parse_md(date_converted)}_'
                        )

                        try:
                            bot.send_message(
                                user.id,
                                text,
                                parse_mode=ParseMode.MARKDOWN_V2,
                            )
                        except BadRequest as error:
                            send_email_error(error, text)
                            print(error)
                            print(text)


def parse_md(text: str) -> str:
    """Adiciona caracteres de escape nos caracteres protegidos.

    Args:
        text (str): Texto sem parse.

    Returns:
        str: Texto com parse.
    """
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
        '[',
        ']',
        '(',
        ')',
        '*',
        '#',
        '_',
    ]

    formated_text = ''
    for char in text:
        if char in special:
            formated_text += f'\\{char}'
        else:
            formated_text += f'{char}'

    return formated_text


def send_email_error(error, message) -> None:
    """Envia um email quando nao conseguir enviar o post para o usuario.

    Args:
        error (BadRequest): Telegram bad request error.
        text (str): Message that cause the error.
    """
    msg = MIMEMultipart()

    msg['From'] = 'regyeduardo+error@gmail.com'
    msg['To'] = 'regyeduardo@gmail.com'
    msg['Subject'] = error.message

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(msg['From'], config('EMAIL'))
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
