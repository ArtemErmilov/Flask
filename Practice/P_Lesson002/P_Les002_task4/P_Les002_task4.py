# Задание №4
# 📌 Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# 📌 При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.

from flask import Flask, request, url_for , redirect
from flask import render_template

app = Flask(__name__) # Создание экземпляра класса


@app.route('/') # Декорирование функции
def hello_world(): # Запускаемая функция при обращение к сайту
    return 'Hello World!'

@app.route('/text/', methods=['GET','POST'])
def text():
    if request.method == 'POST':
        txt = request.form.get('text')
        num = len(txt.split())
        return f'Количество слов в тексте {num}'
    return render_template('text.html')
    
if __name__ == '__main__':
    app.run()