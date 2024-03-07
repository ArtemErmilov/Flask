# Задание №7

# 📌 Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
# 📌 Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
# 📌 Данные о новостях должны быть переданы в шаблон через контекст.

from flask import Flask 
from flask import render_template

app = Flask(__name__) # Создание экземпляра класса


@app.route('/') # Декорирование функции
def hello_world(): # Запускаемая функция при обращение к сайту
    return 'Hello World!'

@app.route('/news/')
def get_news():
    _news = [{ 'tittle_news': 'Новость 1',
                'text_news': 'Текст новости 1',
                'dat_news': 'Дата публикации новости 1',                
                },
                { 'tittle_news': 'Новость 2',
                'text_news': 'Текст новости 2',
                'dat_news': 'Дата публикации новости 2',                
                },
                 { 'tittle_news': 'Новость 3',
                'text_news': 'Текст новости 3',
                'dat_news': 'Дата публикации новости 3',                
                },
                ]
    context = {'news': _news,'tittle':__name__ }
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run()