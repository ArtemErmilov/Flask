# Задание №1
# 📌 Создать базу данных для хранения информации о студентах университета.
# 📌 База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# 📌 В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
# возраст, пол, группа и id факультета.
# 📌 В таблице "Факультеты" должны быть следующие поля: id и название
# факультета.
# 📌 Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# 📌 Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их факультета.

from flask import Flask, render_template

from models_p3t1 import db, Faculties, Students, Gender

app = Flask(__name__) # Создание экземпляра класса

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_p3l1.db' # Подключение БД
db.init_app(app) # Создание БД

@app.cli.command("init-db") # Создание базы данных
def init_db():
    # Покажет ошибку с неверным wsgi.py
    db.create_all()
    print('OK')

@app.route('/') # Декорирование функции
def hello_world(): # Запускаемая функция при обращение к сайту
    return 'Hello World!'

# Создание записей в БД по факультетам.
@app.cli.command("add-faculties")
def add_faculties():
    while(True):
        my_name_faculty = input('Введите название факультета: ')
        faculties =  Faculties(name_faculty = my_name_faculty) # Создание экземпляра с данными.
        db.session.add(faculties) # Добавление сессии с данными пользователя в БД 
        db.session.commit() # Сохранение данных пользователя в БД
        print(faculties)
        in_dat = input('Для выхода нажмите q')
        if (in_dat == 'q'):
            break
        else: continue
    print('Данные по факультетам заполнены!')

# Создание записей в БД по студентам.
@app.cli.command("add-students")
def add_students():
    while(True):
        st_name = input('Введите имя студента: ')
        st_surname = input('Введите фамилию студента: ')
        st_age = input('Введите возраст студента: ')
        my_gender = int(input('Введите пол студента 1 - м, 2 - ж : '))
        if (my_gender == 1):
            st_gender = Gender.male
        elif (my_gender == 2):
            st_gender = Gender.female
        else: st_gender = 0
        st_group = input('Введите номер группы студента: ')
        st_faculty_id = input('Введите ID факультета студента: ')
        students =  Students(name = st_name, surname = st_surname, age = st_age, gender = st_gender, group = st_group, faculty_id = st_faculty_id ) # Создание экземпляра с данными.
        db.session.add(students) # Добавление сессии с данными пользователя в БД 
        db.session.commit() # Сохранение данных пользователя в БД
        print(students)
        in_dat = input('Для выхода нажмите q')
        if (in_dat == 'q'):
            break
        else: continue
    print('Данные по студентам заполнены!')


@app.route('/students/')
def all_students():
    all_students = Students.query.all()
    for con in all_students:
        faculties = Faculties.query.filter(Faculties.id == con.faculty_id).all()
        for d in faculties:
           con.faculty_id=d.name_faculty
    context = {'students': all_students}
    
    return render_template('users.html', **context)

# @app.route('/students/')
# def all_students():
#     all_students = Students.query.all()
#     context = {'students': all_students}
#     for con in all_students:
#         faculties = Faculties.query.filter(Faculties.id == con.faculty_id).all()
#         for d in faculties:
#             print(d.name_faculty)
#     return render_template('users.html', **context)
    

if __name__ == '__main__':
    # app.run()
    # init_db() # При запуске создаётся БД запускается файл wsgi.py и через него запускается файл models_p3t1 и создаются объявленные таблицы.
    # add_faculties()
    add_students()
    # all_students()