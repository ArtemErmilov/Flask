# Задание №1

# Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.


from flask import Flask 
from flask import render_template, url_for

app = Flask(__name__) # Создание экземпляра класса

@app.route('/') 
def first_page(): 
    return render_template('first.html')

@app.route('/next/') 
def next_page(): 
    return render_template('next.html')

if __name__ == '__main__':
    app.run()