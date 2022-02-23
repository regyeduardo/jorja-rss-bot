"""Command botao."""
# from datetime import datetime

# import pytz
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup, ParseMode,
                      Update)
from telegram.ext import CallbackContext


def botao(update: Update, context: CallbackContext):
    """Return message for botao command."""
    print(update.effective_user)
    print(context.user_data)

    def get_gmt(gmt):
        if int(gmt) > 0:
            return f'+{gmt}'
        return gmt

    button_list = [
        [
            InlineKeyboardButton(
                f'Etc/GMT{get_gmt(i-12)}',
                callback_data=f'Etc/GMT{get_gmt(12-i)}',
            )
        ]
        for i in range(25)
    ]

    reply_markup = InlineKeyboardMarkup(button_list)
    update.message.reply_text(
        text='[BRASIL](www.google.com) seu fuso horario',
        reply_markup=reply_markup,
        parse_mode=ParseMode.MARKDOWN_V2,
    )


def responses(update: Update, context: CallbackContext):
    """Callbacks here."""
    # gmt = update.callback_query.data
    # timezone = pytz.timezone(gmt)
    # london = pytz.timezone('Europe/London')
    # time_london = datetime.now().astimezone(london)
    # print(time_london.astimezone(timezone))

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Fuso horario atualizado',
        parse_mode=ParseMode.MARKDOWN_V2,
    )


# text="*bold* _italic_ `fixed width font` [link](http://google.com)\.",
#                  parse_mode=telegram.ParseMode.MARKDOWN_V2)
