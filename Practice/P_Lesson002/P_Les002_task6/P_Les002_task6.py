# Задание №6
# 📌 Создать страницу, на которой будет форма для ввода имени и возраста пользователя 
# и кнопка "Отправить"
# 📌 При нажатии на кнопку будет произв-едена проверка возраста и переход на страницу 
# с результатом или на страницу с ошибкой в случае некорректного возраста.


from flask import Flask, request, url_for , redirect
from flask import render_template

app = Flask(__name__) # Создание экземпляра класса


@app.route('/') # Декорирование функции
def hello_world(): # Запускаемая функция при обращение к сайту
    return 'Hello World!'

@app.route('/error/') 
def error_date(): 
    return render_template('error.html')

@app.route('/user/', methods=['GET','POST'])
def user():
    if request.method == 'POST':
        name = request.form.get('user_num')
        age_user = int(request.form.get('age'))
        if ( name == 'Артём' and age_user == 39 ) or ( name == 'Вова' and age_user == 41 ):
           return f'Данные пользователя {name} введены правильно.'
        else:
            return redirect(url_for('error_date')) # Запуск другой функции
    return render_template('user.html')

if __name__ == '__main__':
    app.run(debug=True)