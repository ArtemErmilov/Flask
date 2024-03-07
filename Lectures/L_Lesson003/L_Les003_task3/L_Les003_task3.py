from flask import Flask, request

from flask_sqlalchemy import SQLAlchemy # Подключение к базе данных
from models_05 import db, User, Post, Comment


app = Flask(__name__) # Создание экземпляра класса

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db' # Подключение БД
db.init_app(app)

@app.route('/')
def index():
    return 'Введи путь к файлу в адресной строке'

@app.cli.command("init-db") # функцию, которая создаст таблицы через консольную команду.
def init_db():
    # Покажет ошибку с неверным wsgi.py
    db.create_all()
    print('OK')

if __name__ == '__main__':
    app.run(debug=True)