from flask import Flask, request

from flask_sqlalchemy import SQLAlchemy # Подключение к базе данных

app = Flask(__name__) # Создание экземпляра класса

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db' # Подключение БД
# Где sqlite: - какая база данных будет использоваться, mydatabase.db - название базы данных

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@hostname/db_name'
# Где mysql - какая база данных будет использоваться, pymysql - библиотека позволяющая питону взаимодействовать с mysql устанавливается через pip, username и password - это логин и пароль для подключения к базе данных, hostname - адрес сервера базы данных, db_name - имя БД.

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopyg2://username:password@hostname/db_name'
@app.route('/')
def index():
    return 'Введи путь к файлу в адресной строке'


if __name__ == '__main__':
    app.run(debug=True)

