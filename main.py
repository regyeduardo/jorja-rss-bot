"""Main module for run the app."""

import asyncio

from sqlalchemy_utils import create_database, database_exists

from duzinho_teste_bot.database import Base, engine
from duzinho_teste_bot.settings import updater

# from duzinho_teste_bot.utils.tasks import get_feeds


async def run_bot():
    """Executa o bot."""
    print('BOT IS RUNNING')
    updater.start_polling()
    await asyncio.sleep(0.1)


if __name__ == '__main__':
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(bind=engine)

    print('BOT IS RUNNING')
    updater.start_polling()
    # def stop():
    #     """Stop the async task."""
    #     task.cancel()

    # loop = asyncio.get_event_loop()
    # # loop.call_later(5, stop) #increase end time as per your requirement
    # # tasks = [loop.create_task(run_bot()), loop.create_task(get_feeds())]
    # # wait_tasks = asyncio.wait(tasks)
    # asyncio.ensure_future(run_bot())
    # # asyncio.ensure_future(get_feeds())
    # loop.run_forever()
