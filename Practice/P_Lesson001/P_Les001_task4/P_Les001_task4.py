# Задание №4
# 📌 Написать функцию, которая будет принимать на вход строку и
# выводить на экран ее длину.

from flask import Flask 

app = Flask(__name__) # Создание экземпляра класса

@app.route('/') # Декорирование функции
def hello_world(): # Запускаемая функция при обращение к сайту
    return 'Hello World!'

@app.route('/<data>/') 
def len_text(data:str):
    return f'Длина строки {data} равняется {len(data)} символов!'
if __name__ == '__main__':
    app.run()