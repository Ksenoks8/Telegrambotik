def main():
    from core import bot
    token = '5815502615:AAEJgn9HgFJNC2Yvo3p27xsgPdWM9NN44hY'
    bot = bot.Bot(token)
    print('Бот запущен')
    bot.infinity_polling()


if __name__ == '__main__':
    main()