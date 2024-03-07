from flask import Flask, request

app = Flask(__name__) # Создание экземпляра класса

@app.route('/')
def index():
    return 'Введи путь к файлу в адресной строке'

@app.route('/get/')
def get():
    if level := request.args.get('level'):
        text = f'Похоже ты опытный игрок, раз имеешь уровень {level}<br>'
    else:
        text = 'Привет, новичок.<br>'
    return text + f'{request.args}'

if __name__ == '__main__':
    app.run()

# Запрос http://127.0.0.1:5000/get/?name=alex&age=13&level=80