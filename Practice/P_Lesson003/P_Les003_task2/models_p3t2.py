# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название факультета.

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum 

# В данном алгоритме происходит создание БД и таблиц в ней 

db = SQLAlchemy()

class Students(db.Model): # Создание таблицы студенты
    id = db.Column(db.Integer, primary_key=True) # ID студента
    name = db.Column(db.String(20), nullable=False) # Имя студента
    surname = db.Column(db.String(20), nullable=False) # Фамилия студента
    group = db.Column (db.Integer, nullable=False) # Номер группы
    email = db.Column(db.String(120), unique=True, nullable=False)
    rating = db.relationship('Rating', backref=db.backref('students'), lazy=True)
    def __repr__(self):
        return f'Данные студента:\nID студента {self.id};\nИмя студента {self.name};\nФамилия студента {self.surname};\nНомер группы{self.group};\nEmail студента {self.email};'

class Lesson(enum.Enum):
    language = 'Русский'
    mathematics = 'Математика'
    physics = 'Физика'
    chemistry = 'Химия'
    literature = 'Литература'
    history = 'История'

class Rating(db.Model): # Создание таблицы Оценки
    id = db.Column(db.Integer, primary_key=True) # ID факультета
    students_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False) # ID студента (Создание связи с другой таблицей)
    lesson_name = db.Column(db.Enum(Lesson), nullable=False) # Название предмета
    rating = db.Column (db.Integer, nullable=False) # Оценка
    def __repr__(self):
        return f'Оценка:\nID - {self.id};\nID студента - {self.students_id};\nНазвание предмета - {self.lesson_name};\nОценка - {self.rating}.'



