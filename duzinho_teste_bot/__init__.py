"""Teste bot."""
import telegram
from decouple import config

__version__ = '0.1.0'
API_KEY = config('TELEGRAM_API_KEY')
bot = telegram.Bot(token=API_KEY)
