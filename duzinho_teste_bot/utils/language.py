"""Display language options."""
import pytz


def get_user_data(timezone: pytz, lang: str = 'en') -> str:
    """
    Retorna os dados do usuario.

    Args
        lang -- O idioma do usuario.

    Returns
        text -- O texto de acordo com o idioma do usuario.
    """
    timezone = str(timezone).replace('_', '\_')
    if lang == 'pt-br':
        text = 'Suas configurações atuais:\nIdioma: **Português**\nFuso\-'
        text += f'horário: **{timezone}**'
        return text
    elif lang == 'es':
        text = 'Su configuración actual:\nEl idioma: **Español**\nZona '
        text += f'horaria: **{timezone}**'
        return text
    else:
        text = 'Your current settings:\nLanguage: **English**\nTimezone: '
        text += f'**{timezone}**'
        return text


def get_default_error_message(lang: str = 'en') -> str:
    """
    Retorna uma mensagem de erro padrao.

    Args
        lang -- O idioma do usuario.

    Returns
        str -- O texto de acordo com o isioma do usuario.

    """
    if lang == 'pt-br':
        return 'Algo deu errado'
    elif lang == 'es':
        return 'Algo salió mal'
    else:
        return 'Something went wrong'


def get_help_set_timezone_command(lang: str = 'en') -> str:
    """
    Retorna as instrucoes para a mudanca de idioma.

    Args
        lang -- O idioma do usuario.

    Returns
        text -- O texto de acordo com o isioma do usuario.

    """
    timezones = 'https://telegra.ph/Available-timezones-02-23'
    if lang == 'pt-br':
        text = 'Para alterar o seu fuso\-horário é necessário utilizar o '
        text += 'comando /set\_timezone com o fuso\-horário desejado\.'
        text += '\nExemplo: /set\_timezone America/Sao\_Paulo\nPara verificar '
        text += 'as opções [clique e veja a lista de fuso\-horários '
        text += f'disponíveis]({timezones})\.'
        return text
    if lang == 'es':
        text = 'Para cambiar su zona horaria debe utilizar el comando '
        text += '/set\_timezone con la zona horaria deseada\. Ejemplo: '
        text += '/set\_timezone America/Bogota\nPara comprobar las opciones '
        text += '[pulse y vea la lista de zonas horarias disponibles]'
        text += f'({timezones})\.'
        return text
    else:
        text = 'To change your time zone you need to use the /set\_timezone '
        text += 'command with the desired timezone\.\nExemple: /set\_timezone '
        text += 'Europe/London\nTo check the options [click and see the list '
        text += f'of available time zones]({timezones})\.'
        return text


def get_successful_update(lang: str = 'en') -> str:
    """
    Retorna uma mensagem de sucesso padrao.

    Args
        lang -- O idioma do usuario.

    Returns
        str -- O texto de acordo com o isioma do usuario.

    """
    if lang == 'pt-br':
        return 'Atualizado com sucesso.'
    if lang == 'es':
        return 'Actualizado con éxito.'
    else:
        return 'Successfully updated.'


def choose_your_language(lang: str = 'en') -> str:
    """
    Retorna uma mensagem para o usuario escolher o idioma.

    Args
        lang -- O idioma do usuario.

    Returns
        str -- O texto de acordo com o isioma do usuario.

    """
    if lang == 'pt-br':
        return 'Escolha seu idioma.'
    if lang == 'es':
        return 'Elija su idioma.'
    else:
        return 'Choose your language.'
