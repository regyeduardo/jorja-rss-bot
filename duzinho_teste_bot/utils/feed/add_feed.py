"""Add neww feeds."""
from datetime import datetime
from time import mktime

from duzinho_teste_bot.database import SessionLocal, Subscription


def add_feed(request, user_id) -> None:
    """Adiciona novos feeds.

    Args:
        request (feedparser): A requisicao da url.
        user_id (str): ID do usuario.
    """
    subs = Subscription()
    subs.title = request.feed.title
    subs.url = request.href
    subs.user_id = user_id

    try:
        last_post = datetime.strptime(
            request.entries[0].published,
            '%a, %d %b %Y %H:%M:%S %z',
        )
        subs.datetime_last_post = last_post
    except ValueError:
        parsed = request.entries[0].published_parsed
        last_post = datetime.fromtimestamp(mktime(parsed))

        subs.datetime_last_post = last_post
    except AttributeError:
        parsed = request.updated_parsed
        last_post = datetime.fromtimestamp(mktime(parsed))
        subs.datetime_last_post = last_post

    session = SessionLocal()
    session.add(subs)
    session.commit()
    session.close()
