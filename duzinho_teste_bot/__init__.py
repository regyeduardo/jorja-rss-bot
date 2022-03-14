"""Teste bot."""
import telegram
from decouple import config

__version__ = '0.1.4'
API_KEY = config('TELEGRAM_API_KEY')
DATABASE_URL = config('DATABASE_URL')


def get_database_connection():
    """Retorna a URL do banco de dados.

    Returns:
        str: URL do banco de dados.
    """
    if 'postgres://' in DATABASE_URL:
        URL = DATABASE_URL.replace('postgres://', 'postgresql://')
        return URL
    else:
        return DATABASE_URL


bot = telegram.Bot(token=API_KEY)
