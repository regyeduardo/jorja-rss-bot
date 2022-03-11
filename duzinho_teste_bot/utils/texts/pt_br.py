"""Textos do idioma Português."""
from .en import EN


class PTBR(EN):
    """Textos em Português.

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
            'Suas configurações atuais:\nIdioma: **Português**\n'
            f'Fuso\-horário: **{self._timezone}**'
        )

        self._default_error = 'Algo deu errado'

        self._help_set_timezone = (
            'Para alterar o seu fuso\-horário é '
            'necessário utilizar o comando /set\_timezone com o fuso\-'
            'horário desejado\.\nExemplo: /set\_timezone America/Sao\_Paulo'
            '\nPara verificar as opções [clique e veja a lista de fuso\-'
            f'horários disponíveis]({self._timezones_list_url})\.'
        )

        self._default_successful_updated = 'Atualizado com sucesso.'
        self._choose_your_language = 'Escolha seu idioma.'
        self._help_add = (
            'Insira /add junto com algum feed válido.'
            '\nExemplo: /add https://techcrunch.com/feed/'
        )

        self._has_feed = 'Esta URL já está na sua lista.'
        self._invalid_feed = 'URL de Feed inválido.'

        self._help_delete = (
            'Insira /delete junto com algum feed URL.\n'
            'Exemplo: /delete https://www.apartmenttherapy.com/main.rss'
        )

        self._cannot_delete = 'Você não havia adicionado este feed'
        self._no_feeds = 'Não há feeds'
