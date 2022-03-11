"""Teste bot."""
import telegram
from decouple import config

__version__ = '0.1.0'
API_KEY = config('TELEGRAM_API_KEY')
DATABASE_URL = config('DATABASE_URL')

bot = telegram.Bot(token=API_KEY)
