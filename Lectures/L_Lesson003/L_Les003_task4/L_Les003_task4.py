from flask import Flask, request

from flask_sqlalchemy import SQLAlchemy # Подключение к базе данных
from models_05 import db, User, Post, Comment


app = Flask(__name__) # Создание экземпляра класса

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db' # Подключение БД
db.init_app(app)

@app.route('/')
def index():
    return 'Привет'

@app.cli.command("init-db") # функцию, которая создаст таблицы через консольную команду.
def init_db():
    # Покажет ошибку с неверным wsgi.py
    db.create_all()
    print('OK')

# Создание записей в БД
@app.cli.command("add-john")
def add_user():
    user = User(username='john', email='john@example.com') # Создание экземпляра с данными.
    db.session.add(user) # Добавление сессии с данными пользователя в БД 
    db.session.commit() # Сохранение данных пользователя в БД
    print('John add in DB!')
    # Для добавления данных в консоли cmd запускаем flask add-john


# Изменение записей
@app.cli.command("edit-john")
def edit_user():
    user = User.query.filter_by(username='john').first() # query - создание запроса, filter_by - фильтрация по username='john', first() - метод, который находит первое совпадение.
    user.email = 'new_email@example.com' # Новый емейл, который будет записан в БД
    db.session.commit()
    print('Данные по mail Джона изменены в БД')

# Удаление записей
@app.cli.command("del-john")
def del_user():
    user = User.query.filter_by(username='john').first()
    db.session.delete(user) # Функция с сессией удаления пользователя 
    db.session.commit() # Сохранение базы данных после удаления пользователя
    print('Delete John from DB!')
    
# Добавление данных в базу данных.
@app.cli.command("fill-db")
def fill_tables():
    count = 5
    # Добавляем пользователей
    for user in range(1, count + 1):
        new_user = User(username=f'user{user}', email=f'user{user}@mail.ru')
        db.session.add(new_user)
    db.session.commit()

    # Добавляем статьи
    for post in range(1, count ** 2):
        author = User.query.filter_by(username = f'user{post % count + 1}').first()
        new_post = Post(title=f'Post title {post}', content=f'Post content {post}', author=author)
        db.session.add(new_post)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)