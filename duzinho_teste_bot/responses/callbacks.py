"""Callback function."""
import pytz
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from ..database import SessionLocal, User


def responses(update: Update, context: CallbackContext) -> None:
    """Callbacks here."""
    # timezone = pytz.timezone(gmt)
    # london = pytz.timezone('Europe/London')
    # time_london = datetime.now().astimezone(london)
    # print(time_london.astimezone(timezone))

    # context.bot.send_message(
    #     chat_id=update.effective_chat.id,
    #     text='Fuso horario atualizado',
    #     parse_mode=ParseMode.MARKDOWN_V2,
    # )
    id = update.effective_chat.id
    response = update.callback_query.data
    update.effective_message.delete()
    session = SessionLocal()

    timezone = pytz.timezone(response)

    user = User()
    user.id = id
    user.language = 'pt-br'
    user.timezone = timezone

    session.add(user)
    session.commit()
