import requests

from config import api_key_weather


def get_weather():
    s_city = input('Введите название города, в котором вы хотите узнать погоду\n'
                   '>>>')
    weather = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': s_city, 'type': 'like', 'units': 'metric', 'appid': api_key_weather}).json()

    try:
        city_name = weather['list'][0]['name']
        main_weather = weather['list'][0]['weather'][0]['main']
        temp = weather['list'][0]['main']['temp']
        pressure = weather['list'][0]['main']['pressure']
        humidity = weather['list'][0]['main']['humidity']
        print(f'В городе {city_name}:\n'
              f'{main_weather}\n'
              f'Температура: {temp} °C\n'
              f'Давление: {pressure} гПа\n'
              f'Влажность: {humidity} %\n')
    except:
        print('Что-то пошло не так...\n')
