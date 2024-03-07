from flask import Flask, render_template

app = Flask(__name__) # Создание экземпляра класса

@app.route('/')
def index():
    return 'Введи путь к файлу в адресной строке'

@app.route('/about/')
def about():
    context = {
    'title': 'Обо мне',
    'name': 'Харитон',
    }
    return render_template('about.html', **context)

if __name__ == '__main__':
    app.run()