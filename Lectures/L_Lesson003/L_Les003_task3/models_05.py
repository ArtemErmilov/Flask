from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
class User(db.Model): # Создание таблицы внутри базы данных
    id = db.Column(db.Integer, primary_key=True)  # Создание ID  с автоматическим присваиванием номера 
    username = db.Column(db.String(80), unique=True, nullable=False) # Колонка строкового вида до 80 символов, unique=True - говорит о том что поле должно быть уникальным, nullable=False - если поле не заполнено то данные не будут сохранены в БД.
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow) # Колонка с типом данных DateTime, default=datetime.utcnow автоматически добавляет время создание при добавление пользователя
    posts = db.relationship('Post', backref='author', lazy=True) # В данной строке происходит понимания к каким статьям принадлежит данный автор

    def __repr__(self): # Метод, который при распечатывание выведет данные пользователя.
        return f'User({self.username}, {self.email})'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False) # Текстовое поле 
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # Происходит ссылание на идентификатор автора статьи 
    created_at = db.Column(db.DateTime, default=datetime.utcnow) # Время создания статьи 

    def __repr__(self):
        return f'Post({self.title}, {self.content})'

# Создание связей между моделями

class Comment(db.Model): # Создание таблицы комментария к статье
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False) # Строка комментария
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False) # Привязка комментария к ID статьи (Создание связи с другой таблицей)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # Привязка комментария к ID автора комментария (Создание связи с другой таблицей)
    created_at = db.Column(db.DateTime, default=datetime.utcnow) # Время создания комментария
    def __repr__(self):
        return f'Comment({self.content})'