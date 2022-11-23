from kitty_func import get_kitty
from news_func import get_article
from weather_func import get_weather

while True:
    to_do = input('Чтобы узнать погоду, введите 1\n'
                  'Чтобы найти новостную статью, введите 2\n'
                  'Чтобы запустить генератор котиков, введите 3\n'
                  '>>>')
    if to_do == '1':
        get_weather()
    elif to_do == '2':
        get_article()
    elif to_do == '3':
        print('Чтобы потом продолжить выполнение этого скрипта, закройте открывшееся окно')
        get_kitty()
    else:
        print('Вы ввели что-то не то...\n'
              'Попробуйте снова\n'
              '>>>')
