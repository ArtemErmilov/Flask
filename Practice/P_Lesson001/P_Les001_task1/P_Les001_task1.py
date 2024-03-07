from flask import Flask 

app = Flask(__name__) # Создание экземпляра класса

@app.route('/') # Декорирование функции
def hello_world(): # Запускаемая функция при обращение к сайту
    return 'Hello World!'


if __name__ == '__main__':
    app.run()