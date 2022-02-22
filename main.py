"""Main module for run the app."""

from duzinho_teste_bot.settings import updater

if __name__ == '__main__':
    print('BOT IS RUNNING')
    updater.start_polling()
