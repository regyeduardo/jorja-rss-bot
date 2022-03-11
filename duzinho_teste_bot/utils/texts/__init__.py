from .en import EN
from .es import ES
from .pt_br import PTBR


def get_language_texts(language: str) -> any:
    """Recebe o idioma do usuário e retorna o módulo que contém os textos
    de desse idioma.

    Args:
        language (str): Idioma do usuário.

    Returns:
        any: O módulo correto com os textos do idioma.
    """
    if language == 'pt-br':
        return PTBR
    elif language == 'es':
        return ES
    else:
        return EN
