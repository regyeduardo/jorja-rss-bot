"""

Este modulo contem metodos que trabalham?
com fuso horarios em GMT.
"""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

from .. import bot


def get_correct_gmt(gmt: str) -> str:
    """
    Recebe uma string que e um
    numero em string e converte
    em string com um mais (+) se
    o numero for positivo.
    """
    if int(gmt) > 0:
        return f'+{gmt}'
    return gmt


def return_gmt_buttons(
    chat_id: int, text: str = 'Escolha seu fuso horario'
) -> None:
    """Return button."""
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
