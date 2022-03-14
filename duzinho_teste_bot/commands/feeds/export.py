"""Export comand."""
import xml.etree.ElementTree as ET  # nosec
from io import BytesIO

# from defusedxml import ElementTree as ET
from telegram import Update
from telegram.ext import CallbackContext

from duzinho_teste_bot.database import SessionLocal, Subscription


def export(update: Update, context: CallbackContext) -> None:
    """Exporta os feeds do usuario em um arquivo opml.

    Args:
        update (Update): Class from telegram.
        context (CallbackContext): Class from telegram.
    """
    fake_file = BytesIO()
    opml = ET.Element('opml')

    head = ET.SubElement(opml, 'head')
    head_title = ET.SubElement(head, 'title')
    head_title.text = 'OPML file from Jorja Rss Bot'

    body = ET.SubElement(opml, 'body')

    session = SessionLocal()
    chat_id = str(update.effective_chat.id)
    subs = (
        session.query(Subscription)
        .filter(Subscription.user_id == chat_id)
        .all()
    )
    session.close()
    for sub in subs:
        title = sub.title
        url = sub.url
        outline = ET.SubElement(body, 'outline')
        outline.set('text', title)
        outline.set('title', title)
        outline.set('type', 'rss')
        outline.set('xmlUrl', url)

    et = ET.ElementTree(opml)

    ET.indent(et, space='\t', level=0)
    et.write(fake_file, encoding='utf-8', xml_declaration=True)

    context.bot.send_document(
        chat_id, document=fake_file.getvalue(), filename='feeds.opml'
    )
