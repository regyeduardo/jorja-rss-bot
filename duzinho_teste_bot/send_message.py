"""Send custom message."""
from . import bot


def send_custom_message(message: str, chat: int) -> None:
    """Send message to a custom chat."""
    bot.send_message(text=message, chat_id=chat)
