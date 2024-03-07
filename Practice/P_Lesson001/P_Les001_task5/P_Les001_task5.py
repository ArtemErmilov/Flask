# Задание №5
# 📌 Написать функцию, которая будет выводить на экран HTML
# страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!".

from flask import Flask 

app = Flask(__name__) # Создание экземпляра класса

@app.route('/') # Декорирование функции
def hello_world(): # Запускаемая функция при обращение к сайту
    return 'Hello World!'

@app.route('/text/') 
def output_text(): 
    return '<h1>Моя первая HTML страница</h1><p>Привет, мир!</p>'

if __name__ == '__main__':
    app.run()