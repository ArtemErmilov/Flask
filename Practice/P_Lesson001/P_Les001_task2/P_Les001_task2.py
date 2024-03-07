# Задание №2
# 📌 Добавьте две дополнительные страницы в ваше веб-приложение:
#   ○ страницу "about"
#   ○ страницу "contact".

from flask import Flask, render_template


app = Flask(__name__) # Создание экземпляра класса

@app.route('/') # Декорирование функции
def main_start(): # Запускаемая функция при обращение к сайту
    return 'Привет!!!'

@app.route('/about/') # Декорирование функции
def about(): # Запускаемая функция при обращение к сайту
    return render_template('about.html')

@app.route('/contact/') # Декорирование функции
def contact(): # Запускаемая функция при обращение к сайту
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()