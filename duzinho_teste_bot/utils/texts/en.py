"""Textos do idioma Inglês."""


class EN:
    """Textos em Inglês."""

    def __init__(self, user):
        """Método construtor da classe.

        Args:
            user (User): Instância da classe User.
        """
        self._user = user

        self._timezones_list_url = str(
            'https://telegra.ph/Available-timezones-02-23'
        )

        self._timezone = str(self._user.timezone).replace('_', '\_')

        self._user_data = (
            'Your current settings:'
            f'\nLanguage: **English**\nTimezone: {self._timezone}'
        )

        self._default_error = 'Something went wrong'

        self._help_set_timezone = (
            'To change your time zone you need to use the /set\_timezone '
            'command with the desired timezone\.\nExemple: /set\_timezone '
            'Europe/London\nTo check the options [click and see the list '
            f'of available time zones]({self._timezones_list_url})\.'
        )

        self._default_successful_updated = 'Successfully updated.'
        self._choose_your_language = 'Choose your language.'

        self._help_add = (
            'Insert /add along with some valid url.\nExample: '
            '/add https://techcrunch.com/feed/'
        )

        self._has_feed = 'This URL is already in your list.'
        self._invalid_feed = 'Invalid URL feed.'

        self._help_delete = (
            'Insert /delete along with some feed URL.\n'
            'Exemple: /delete https://www.apartmenttherapy.com/main.rss'
        )

        self._cannot_delete = 'You had not added this feed.'
        self._no_feeds = 'There are no feeds'

    @property
    def user_data(self) -> str:
        """Retorna alguns dados do usuário.

        Returns:
            str: Alguns dados salvos do usuário.
        """
        return self._user_data

    @property
    def default_error(self) -> str:
        """Retorna uma mensagem de erro padrão.

        Returns:
            str: Mensagem de erro padrão.
        """
        return self._default_error

    @property
    def help_set_timezone(self) -> str:
        """Retorna uma mensagem de ajuda para o comando set_timezone.

        Returns:
            str: Mensagem de ajuda do comando set_timezone.
        """
        return self._help_set_timezone

    @property
    def default_successful_updated(self) -> str:
        """Retorna uma mensagem de sucesso padrão.

        Returns:
            str: Mensagem de sucesso padrão.
        """
        return self._default_successful_updated

    @property
    def choose_your_language(self) -> str:
        """Retorna uma mensagem para o usuário escolher um idioma.

        Returns:
            str: Mensagem para o usuário escolher um idioma.
        """
        return self._choose_your_language

    @property
    def help_add(self) -> str:
        """Retorna uma mensagem de ajuda para o comando /add.

        Returns:
            str: Mensagem de ajuda para o comando /add.
        """
        return self._help_add

    @property
    def has_feed(self) -> str:
        """Retorna uma mensagem caso o usuário tentar adicionar um feed
        que já exista em sua lista.

        Returns:
            str: Mensagem avisando que o usuário já possui o feed que está
            tentando adicionar no momento.
        """
        return self._has_feed

    @property
    def invalid_feed(self) -> str:
        """Retorna uma mensagem caso o usuário tentar adicionar um URL de
        feed inválido.

        Returns:
            str: Mensagem avisando que o feed é inválido.
        """
        return self._invalid_feed

    @property
    def help_delete(self) -> str:
        """Ajuda para o comando /delete.

        Returns:
            str: Mensagem mostrando um exemplo de uso do comando /delete.
        """
        return self._help_delete

    @property
    def cannot_delete(self) -> str:
        """Retorna uma mensagem avisando que o usuário está tentando
        deletar um feed inexistente em sua lista.

        Returns:
            str: Mensagem avisando que não é possível deletar,
        """
        return self._cannot_delete

    @property
    def no_feeds(self) -> str:
        """Retorna uma mensagem avisando que o usuário não possui nenhum feed
        em sua lista.

        Returns:
            str: Mensagem avisando que não há feeds na lista.
        """
        return self._no_feeds
