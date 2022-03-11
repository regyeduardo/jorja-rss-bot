"""Test echo method."""
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import CallbackContext

from duzinho_teste_bot.database import SessionLocal, User
from duzinho_teste_bot.utils import flags, get_language_texts


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

        lang = get_language_texts(user.language)(user)
        try:
            session.add(user)
            session.commit()
            session.close()
            text = lang.default_successful_updated
            context.bot.send_message(
                chat_id, text, reply_markup=ReplyKeyboardRemove()
            )
        except:  # pylint: disable=bare-except
            text = lang.default_error
            context.bot.send_message(chat_id, text)

    # else:
    #     text = f'Falou: {update.message.text}?'
    #     context.bot.send_message(chat_id=chat_id, text=text)
