# Задание №5
# 📌 Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"

# 📌 При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.

from flask import Flask, request, url_for , redirect
from flask import render_template

app = Flask(__name__) # Создание экземпляра класса


@app.route('/') # Декорирование функции
def hello_world(): # Запускаемая функция при обращение к сайту
    return 'Hello World!'

@app.route('/add/', methods=['GET','POST'])
def add_num():
    if request.method == 'POST':
        num1 = int(request.form.get('num1'))
        num2 = int(request.form.get('num2'))
        if request.form.get('math_num')=='add':
           num = num1 + num2
           return f'Сумма чисел равняется {num}'
        elif request.form.get('math_num') == 'sub':
            num = num1 - num2
            return f'Разность чисел равняется {num}'
        elif request.form.get('math_num') == 'mul':
            num = num1 * num2
            return f'Произведение чисел равняется {num}'
        elif request.form.get('math_num') == 'dif':
            num = float(num1) / float(num2)
            return f'Деление чисел равняется {num}'
        else:
            return 'Математическая операция не выбрана!'
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)