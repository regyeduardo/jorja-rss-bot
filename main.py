"""Main module for run the app."""

import asyncio

from sqlalchemy_utils import create_database, database_exists

from duzinho_teste_bot.database import Base, engine
from duzinho_teste_bot.settings import updater
from duzinho_teste_bot.utils.tasks import get_feeds

if __name__ == '__main__':
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(engine)

    def stop():
        """Stop the async task."""
        task.cancel()

    loop = asyncio.get_event_loop()
    # loop.call_later(5, stop) #increase end time as per your requirement
    task = loop.create_task(get_feeds())

    try:
        loop.run_until_complete(task)
    except asyncio.CancelledError:
        pass

    print('BOT IS RUNNING')
    updater.start_polling()
