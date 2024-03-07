# Задание №9
# 📌 Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# 📌 Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.

from flask import Flask
from flask import render_template
app = Flask(__name__)



@app.route('/')
def index():
    context = {'title': 'Главная'}
    return render_template('index.html',**context)
    
@app.route('/cloth/')
def cloth():
    context = {'title': 'Одежда'}
    return render_template('cloth.html', **context)

@app.route('/jacket/')
def jackets():
    return render_template('jacket.html')

@app.route('/trousers/')
def trousers():
    return render_template('trousers.html')



@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    return render_template('shoes.html', **context)


@app.route('/boots/')
def boots():
    return render_template('boots.html')

@app.route('/slippers/')
def slippers():
    return render_template('slippers.html')

if __name__ == '__main__':
    app.run(debug=True)