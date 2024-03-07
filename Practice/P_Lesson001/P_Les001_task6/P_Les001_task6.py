# Задание №6
# 📌 Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах.
# 📌 Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# 📌 Данные о студентах должны быть переданы в шаблон через контекст.

from flask import Flask 

app = Flask(__name__) # Создание экземпляра класса
from flask import render_template

@app.route('/') # Декорирование функции
def hello_world(): # Запускаемая функция при обращение к сайту
    return 'Hello World!'

@app.route('/users/')
def students():
    _students = [{ 'name': 'Артём',
                'surname': 'Ермилов',
                'age': '39',
                'GPA': '4.3',                
                },
                { 'name': 'Владимир',
                'surname': 'Самойлов',
                'age': '41',
                'GPA': '5',                
                },
                { 'name': 'Андрей',
                'surname': 'Горский',
                'age': '41',
                'GPA': '3.5',                
                },
                ]
    context = {'students': _students}
    return render_template('index.html', **context)



if __name__ == '__main__':
    app.run()