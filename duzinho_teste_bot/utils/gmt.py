"""Este modulo contem metodos que trabalham. com fuso horarios em GMT."""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

from duzinho_teste_bot import bot


def get_correct_gmt(number: str) -> str:
    """
    Retorna um numero GMT correto.

    Args:
        number (str) -- Um numero inteiro em string.

    Returns:
        number (str) -- Caso o numero seja inteiro ira retorna-lo com um
        (+) mais na frente e caso nao seja ira retornar ele mesmo.
    """
    if int(number) > 0:
        return f'+{number}'
    return number


def return_gmt_buttons(
    chat_id: int, text: str = 'Escolha seu fuso horario'
) -> None:
    """
    Apresenta as opcoes de fuso-horario no chat.

    Args:
        chat_id (int) -- A identificacao do chat.
        text (str) -- O texto que sera apresentado antes da lista de botoes.
    """
    buttons = [
        [
            InlineKeyboardButton(
                f'Etc/GMT{get_correct_gmt(i-12)}',
                callback_data=f'Etc/GMT{get_correct_gmt(12-i)}',
            )
        ]
        for i in range(25)
    ]

    prepared_buttons = InlineKeyboardMarkup(buttons)

    bot.send_message(
        text=text,
        chat_id=chat_id,
        reply_markup=prepared_buttons,
        parse_mode=ParseMode.MARKDOWN_V2,
    )
