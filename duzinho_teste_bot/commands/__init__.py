"""Module for bot commands."""
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater

from .ehoph import ehoph
from .hello import hello
from .start import start
from .wesley import wesley
