# Задание №3
# 📌 Создать страницу, на которой будет форма для ввода логина
# и пароля
# 📌 При нажатии на кнопку "Отправить" будет произведена
# проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с
# ошибкой.

from flask import Flask, request, url_for , redirect
from flask import render_template

app = Flask(__name__) # Создание экземпляра класса


@app.route('/') # Декорирование функции
def hello_world(): # Запускаемая функция при обращение к сайту
    return 'Hello World!'

@app.route('/next/') 
def next_page(): 
    return render_template('next.html')

@app.route('/user/', methods=['GET','POST'])
def auth():
    if request.method == 'POST':
        user_name = request.form.get('login')
        user_pass = request.form.get('pass')
        if  user_name == 'admin' and user_pass == 'pass':
            return 'Hi, boss!'
        else:
             return redirect(url_for('next_page'))
    return render_template('user.html')   


if __name__ == '__main__':
    app.run(debug=True)