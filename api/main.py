import requests
import os
from dotenv import load_dotenv

def get_puplic_data():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1/posts')
    for idx, data in enumerate(response.json()):
        if idx == 5:
            break
        print('Пост: {0}\n{1}\n'.format(
            data['title'],
            data['body']
        ))

def get_weather():
    city = input("Введите название города: ")

    params = {
        'q': city,
        'appid': os.getenv('API_KEY'),
        'units': 'metric',
        'lang': 'ru'
    }

    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"Текущая температура в городе {city}: {temp}°C")
        print(f"Описание погоды: {description}")
    else:
        print(f"Ошибка: {response.status_code}")

def create_post():
    data = {
        "title": "TITLE",
        "body": "LOL\n"
    }
    response = requests.post('https://jsonplaceholder.typicode.com/todos/1/posts', data=data)
    print(response.json())


def main():
    # load_dotenv()
    # get_weather()
    create_post()

if __name__ == '__main__':
    main()