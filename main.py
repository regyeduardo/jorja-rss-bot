"""Main module for run the app."""

from sqlalchemy_utils import create_database, database_exists

from duzinho_teste_bot.database import Base, engine
from duzinho_teste_bot.settings import updater

if __name__ == '__main__':
    if not database_exists(engine.url):
        create_database(engine.url)
        Base.metadata.create_all(engine)

    print('BOT IS RUNNING')
    updater.start_polling()
