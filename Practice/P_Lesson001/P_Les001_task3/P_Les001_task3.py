# Задание №3
# 📌 Написать функцию, которая будет принимать на вход два
# числа и выводить на экран их сумму.

from flask import Flask

app = Flask(__name__) # Создание экземпляра класса

@app.route('/') # Декорирование функции
def hello_world(): # Запускаемая функция при обращение к сайту
    return 'Привет человек'

@app.route('/<data>/')
def hello(data:str):
    dat = data.split("_")
    num = 0
    for d in dat:
        num += int(d)
    return f'Сумма введённых чисел равняется {num}'

@app.route('/sum/<int:a>/<int:b>')
def may_sum(a:int, b:int):
    
    return f'Сумма введённых чисел {a} + {b} = {a+b}'

if __name__ == '__main__':
    app.run()