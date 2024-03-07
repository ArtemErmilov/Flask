from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'

@app.route('/redirect/')
def redirect_to_index():
    return redirect(url_for('index')) # Переход на стартовую странице index

@app.route('/external')
def external_redirect():
    return redirect('https://google.com') # Переход на другой сайт

@app.route('/hello/<name>')
def hello(name):
    return f'Привет, {name}!' # Вывод имени в консоль

@app.route('/redirect/<name>')
def redirect_to_hello(name):
    return redirect(url_for('hello', name=name)) # Переход на функцию @app.route('/hello/<name>')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=False)

