"""Callback files."""
import os

import feedparser
# import xml.etree.ElementTree as ET
# from xml.etree.ElementTree import ParseError
from defusedxml.ElementTree import ParseError, parse
from sqlalchemy.exc import IntegrityError
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from duzinho_teste_bot.utils import add_feed, parse_md


def callback_import_command(update: Update, context: CallbackContext) -> None:
    """Import feeds rss externos.

    Args:
        update (Update): Class from telegram.
        context (CallbackContext): Class from telegram.

    Raises:
        Invalido: Generico.
        Invalido: Generico.

    Yields:
        ElementTree: Cada elemtento que possui feed url.
    """
    chat_id = str(update.effective_chat.id)
    file = context.bot.get_file(update.message.document).download()
    tree = parse(file)
    os.remove(file)
    root = tree.getroot()
    outlines = None
    categories = {'repeated': {}, 'added': {}, 'invalid': {}}

    try:
        outlines = root.findall('.//outline[@xmlUrl]')

        def get_outlines():
            """Gera os elementos que possem feed url.

            Yields:
                ElementTree: Cada elemtento que possui feed url.
            """
            yield from outlines

        for outline in get_outlines():
            title = outline.attrib.get('title')
            url = outline.attrib.get('xmlUrl')

            request = feedparser.parse(url)

            if request.bozo:
                categories['invalid'].update({title: url})
                continue

            try:
                add_feed(request, chat_id)
                categories['added'].update({title: url})
            except IntegrityError:
                categories['repeated'].update({title: url})
    except ParseError:
        context.bot.send_message(chat_id, 'Arquivo invalido')

    text = get_result_text(categories)
    context.bot.send_message(chat_id, text, parse_mode=ParseMode.MARKDOWN_V2)


def get_result_text(categories):
    """Retorna um texto com os feeds categorizados de acordo
    com o resultado em markdown.

    Args:
        categories (dict): Categorias com as feeds.

    Returns:
        str: Texto com os feeds categorizados de acordo com o resultado.
    """
    text = ''
    for category in categories.items():
        if not category[1].items():
            continue

        category_title = f'{parse_md(category[0].capitalize())}:\n'
        text += category_title

        for category_element in category[1].items():
            title = category_element[0]
            url = category_element[1]

            text += f'[{parse_md(title)}]({parse_md(url)})\n'

    return text
