from flask import Flask, request

from flask_sqlalchemy import SQLAlchemy # Подключение к базе данных
from models_02 import db



app = Flask(__name__) # Создание экземпляра класса

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db' # Подключение БД
db.init_app(app)

@app.route('/')
def index():
    return 'Введи путь к файлу в адресной строке'


if __name__ == '__main__':
    app.run(debug=True)