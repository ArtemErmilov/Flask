# Задание №3
# 📌 Доработаем задача про студентов
# 📌 Создать базу данных для хранения информации о студентах и их оценках в учебном заведении.
# 📌 База данных должна содержать две таблицы: "Студенты" и "Оценки".
# 📌 В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
# 📌 В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
# 📌 Необходимо создать связь между таблицами "Студенты" и "Оценки".
# 📌 Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их оценок.

from flask import Flask 
from flask import render_template,jsonify
import random
from models_p3t2 import db, Students, Rating, Lesson

app = Flask(__name__) # Создание экземпляра класса

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_p3l2.db' # Подключение БД
db.init_app(app) # Создание БД

@app.cli.command("init-db") # Создание базы данных
def init_db():
    # Покажет ошибку с неверным wsgi.py
    db.create_all()
    print('OK')

@app.cli.command("add-students") # Добавление данных по студентам
def add_students():
    max_id = 0
    all_students = Students.query.all()
    for id_s in all_students:
        max_id = id_s.id
    repeat = random.randint(5,11)
    for ind in range (1, repeat+1):
        name_ar = ['Артём', 'Владимер', 'Александер', 'Андрей', 'Ярослав']
        surname_ar = ['Ермилов', 'Самойлов', 'Горский', 'Петров', 'Иванов']
        st_name = random.choice(name_ar)
        st_surname = random.choice(surname_ar)
        st_group = random.randint(100,601)
        st_email = f'mail{max_id+ind}@mail.com'
        students =  Students(name = st_name, surname = st_surname, group = st_group, email = st_email )
        db.session.add(students) # Добавление сессии с данными пользователя в БД 
        db.session.commit() # Сохранение данных пользователя в БД
        print(students)
    

@app.cli.command("add-rating") # Добавление данных по оценкам
def add_rating():
    les_ar = [Lesson.language,Lesson.chemistry,Lesson.history,Lesson.literature,Lesson.mathematics,Lesson.physics]
    all_students = Students.query.all()
    for id_s in all_students:
        max_id_st = id_s.id
    print(max_id_st)
    for stu_id in range(1, max_id_st+1):
        max_rating = random.randint(6,13)
        for _ in range (max_rating):
            ra_lesson_name = random.choice(les_ar)
            ra_rating = random.randint (1,5)
            rating =  Rating(students_id = stu_id,lesson_name = ra_lesson_name,rating = ra_rating)
            db.session.add(rating) # Добавление сессии с данными пользователя в БД 
            db.session.commit() # Сохранение данных пользователя в БД
    print('База с оценками заполнена!!!')


@app.route('/') # Декорирование функции
def hello_world(): # Запускаемая функция при обращение к сайту
    return 'Hello World!'

@app.route('/students/') # Вывод данных по студентам в HTML 
# @app.cli.command("print-students")
def in_students():
    all_students = Students.query.all()
    for id_s in all_students:
        id_st = id_s.id
        les_ar = [Lesson.language,Lesson.chemistry,Lesson.history,Lesson.literature,Lesson.mathematics,Lesson.physics]        
        print( f'{id_s.name} {id_s.surname}')
        for data in les_ar:
            rating = Rating.query.filter_by(students_id=id_st).filter_by(lesson_name = data).all()
            rat = ''
            for r in rating:
                rat = f'{rat} {r.rating},'
            les = f'{data}: {rat}'
            print(les)
            lis_rat = {data : les}
        data_temp = jsonify({'name' : id_s.name, 'surname' : id_s.surname, 'lesson':lis_rat})
    context = {'students': data_temp}
    return render_template('users.html', **context)
        
    # if  all_students:
    #     return jsonify([{'id': student.id, 'name': student.name, 'surname': student.surname, 'group': student.group, 'email': student.email, } for student in all_students])
    # else:
    #     return jsonify({'error': 'Posts not found'}), 404


if __name__ == '__main__':

    temp = int(input('Выбрать действия: 1 - создание БД, 2 - ввод данных по студентам, 3 - ввод данных по оценкам, 4 - запуск html:\n'))
    if (temp==1):
        init_db()
    elif (temp==2):
        add_students()
    elif (temp==3):
        add_rating()
    elif (temp==4):
        # in_students()
        app.run(debug=True)
    else:
        print('Вы не чего не выбрали!!!')