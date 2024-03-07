from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
class User(db.Model): # Создание таблицы внутри базы данных
    id = db.Column(db.Integer, primary_key=True)  # Создание ID  с автоматическим присваиванием номера 
    username = db.Column(db.String(80), unique=True, nullable=False) # Колонка строкового вида до 80 символов, unique=True - говорит о том что поле должно быть уникальным, nullable=False - если поле не заполнено то данные не будут сохранены в БД.
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow) # Колонка с типом данных DateTime, default=datetime.utcnow автоматически добавляет время создание при добавление пользователя

    def __repr__(self): # Метод, который при распечатывание выведет данные пользователя.
        return f'User({self.username}, {self.email})'