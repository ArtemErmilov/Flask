# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название факультета.

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum 

# В данном алгоритме происходит создание БД и таблиц в ней 

db = SQLAlchemy()

class Gender(enum.Enum):
    male = 'м'
    female = 'ж'

class Faculties(db.Model): # Создание таблицы факультеты со столбцами 
    id = db.Column(db.Integer, primary_key=True) # ID факультета
    name_faculty = db.Column(db.String(100), unique=True, nullable=False) # Название факультета
    students = db.relationship('Students', backref=db.backref('faculties'), lazy=True)
    def __repr__(self):
        return f'Данные факультета: ID - {self.id}, название - {self.name_faculty}.'

class Students(db.Model): # Создание таблицы студенты
    id = db.Column(db.Integer, primary_key=True) # ID студента
    name = db.Column(db.String(20), nullable=False) # Имя студента
    surname = db.Column(db.String(20), nullable=False) # Фамилия студента
    age = db.Column(db.Integer, nullable=False) # Возраст студента.
    # gender = db.Column (db.String(1), nullable=False) # Пол
    gender = db.Column (db.Enum(Gender), nullable=False) # Пол
    group = db.Column (db.Integer, nullable=False) # Номер группы
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculties.id'), nullable=False) # Ссылка на id факультета.
    def __repr__(self):
        return f'Данные студента:\nID студента{self.id};\nИмя студента{self.name};\nФамилия студента{self.surname};\nВозраст студента{self.age} лет;\nПол студента{self.gender};\nНомер группы{self.group};\nФакультет ID{self.faculty_id};'
    

# class User(db.Model): # Создание таблицы внутри базы данных
#     id = db.Column(db.Integer, primary_key=True)  # Создание ID  с автоматическим присваиванием номера primary_key=True - ячейка заполняется автоматически.
#     username = db.Column(db.String(80), unique=True, nullable=False) # Колонка строкового вида до 80 символов, unique=True - говорит о том что поле должно быть уникальным, nullable=False - если поле не заполнено то данные не будут сохранены в БД.
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow) # Колонка с типом данных DateTime, default=datetime.utcnow автоматически добавляет время создание при добавление пользователя
#     posts = db.relationship('Post', backref='author', lazy=True) # В данной строке происходит понимания к каким статьям принадлежит данный автор

#     def __repr__(self): # Метод, который при распечатывание выведет данные пользователя.
#         return f'User({self.username}, {self.email})'

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     content = db.Column(db.Text, nullable=False) # Текстовое поле, 
#     author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # Происходит ссылание на идентификатор автора статьи 
#     created_at = db.Column(db.DateTime, default=datetime.utcnow) # Время создания статьи 

#     def __repr__(self):
#         return f'Post({self.title}, {self.content})'

# # Создание связей между моделями

# class Comment(db.Model): # Создание таблицы комментария к статье
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text, nullable=False) # Строка комментария
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False) # Привязка комментария к ID статьи (Создание связи с другой таблицей)
#     author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # Привязка комментария к ID автора комментария (Создание связи с другой таблицей)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow) # Время создания комментария
#     def __repr__(self):
#         return f'Comment({self.content})'