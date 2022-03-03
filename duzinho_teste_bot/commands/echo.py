"""Test echo method."""
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import CallbackContext

from ..database.db import SessionLocal
from ..database.models.users import User
from ..utils import flags
from ..utils.language import get_default_error_message, get_successful_update


def echo(update: Update, context: CallbackContext):
    """
    Retorna a mensagem do usuario caso nao for um opcao de idioma.

    Args:
        update -- Tipo Update do pacote telegram.
        context -- Tipo CallbackContext do pacote telegram.ext.
    """
    chat_id = str(update.effective_chat.id)
    if update.message.text in flags:
        response = update.message.text
        session = SessionLocal()
        user = session.query(User).filter(User.id == chat_id).first()
        if 'Español' in response:
            user.language = 'es'
        elif 'Português' in response:
            user.language = 'pt-br'
        else:
            user.language = 'en'

        try:
            session.add(user)
            session.commit()
            text = get_successful_update(user.language)
            context.bot.send_message(
                chat_id, text, reply_markup=ReplyKeyboardRemove()
            )
        except:  # pylint: disable=bare-except
            text = get_default_error_message(user.language)
            context.bot.send_message(chat_id, text)

    else:
        text = f'Falou: {update.message.text}?'
        context.bot.send_message(chat_id=chat_id, text=text)
