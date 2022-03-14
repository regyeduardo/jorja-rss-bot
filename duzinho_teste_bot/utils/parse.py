"""Parse functions."""


def parse_md(text: str) -> str:
    """Adiciona caracteres de escape nos caracteres protegidos.

    Args:
        text (str): Texto sem parse.

    Returns:
        str: Texto com parse.
    """
    special = [
        '~',
        '`',
        '>',
        '+',
        '-',
        '=',
        '|',
        '{',
        '}',
        '.',
        '!',
        '[',
        ']',
        '(',
        ')',
        '*',
        '#',
        '_',
    ]

    formated_text = ''
    for char in text:
        if char in special:
            formated_text += f'\\{char}'
        else:
            formated_text += f'{char}'

    return formated_text
