"""Run get_get_feeds."""
import asyncio

from duzinho_teste_bot.utils.tasks import get_feeds

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(get_feeds())
    # asyncio.ensure_future(get_feeds())
    loop.run_forever()
