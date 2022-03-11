"""Textos do idioma Espanhol."""
from .en import EN


class ES(EN):
    """Textos em Espanhol.

    Args:
        EN (EN): Extendendo a class EN para herdar alguns métodos
        para determinados textos
    """

    def __init__(self, user):
        """Método construtor da classe.

        Args:
            user (User): Instância da classe User.
        """
        super().__init__(user)

        self._user_data = (
            'Su configuración actual:\nEl idioma: **Español**'
            f'\nZona horaria: **{self._timezone}**'
        )

        self._default_error = 'Algo salió mal'

        self._help_set_timezone = (
            'Para cambiar su zona horaria debe '
            'utilizar el comando /set\_timezone con la zona horaria '
            'deseada\. \nEjemplo: /set\_timezone America/Bogota\nPara '
            'comprobar las opciones [pulse y vea la lista de zonas horarias '
            f'disponibles]({self._timezones_list_url})\.'
        )

        self._default_successful_updated = 'Actualizado con éxito.'
        self._choose_your_language = 'Elija su idioma.'

        self._help_add = (
            'Insertar /add junto con alguna url válida.\n'
            'Ejemplo: /add https://techcrunch.com/feed/'
        )

        self._has_feed = 'Esta URL ya está en su lista.'
        self._invalid_feed = 'URL inválida.'

        self._help_delete = (
            'Insertar /delete junto con alguna URL.\n'
            'Ejemplo: /delete https://www.apartmenttherapy.com/main.rss'
        )

        self._cannot_delete = 'No habías añadido este feed.'
        self._no_feeds = 'No hay feeds'
