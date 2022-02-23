"""Command set_timezone."""
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

# from . import list_timezones


def set_timezone(update: Update, context: CallbackContext):
    """Return message for ehoph command."""
    text = 'Por favor digite o fuso horario que seja mais adequado para voce, '
    text += '[voce pode encontrar a lista completa de fuso horarios'
    text += 'clicando aqui]'
    text += '(https://telegra.ph/Available-timezones-02-23)'
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        parse_mode=ParseMode.MARKDOWN_V2,
    )
