import requests

from config import api_key_news


def get_article():
    headline = input('Введите ключевое слово для поиска статьи\n'
                     '>>>')
    news = requests.get('https://newsapi.org/v2/everything',
                        params={'q': headline, 'apiKey': api_key_news, 'sort_by': 'relevancy'}).json()

    result_count = news['totalResults']
    if result_count != 0:
        article = news['articles'][0]
        source = article['source']['name']
        author = article['author']
        title = article['title']
        description = article['description']
        url = article['url']
        print(f'\nВсего статей найдено: {result_count}\n\n'
              f'Самая популярная из них:\n\n'
              f'Автор: {author}\n'
              f'Источник: {source}\n'
              f'Название: {title}\n'
              f'Описание: {description}\n'
              f'Прочитать можно по ссылке: {url}')
    else:
        print('Ничего не найдено...\n')
