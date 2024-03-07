from flask import Flask 

app = Flask(__name__) # Создание экземпляра класса

@app.route('/')
@app.route('/<name>/')
def hello(name='незнакомец'):
    return 'Привет, ' + name + '!'

@app.route('/file/<path:file>/')
def set_path(file):
    print(type(file))
    return f'Путь до файла "{file}"'

@app.route('/number/<float:num>/')
def set_number(num):
    print(type(num))
    return f'Передано число {num}'

if __name__ == '__main__':
    app.run(debug=True)