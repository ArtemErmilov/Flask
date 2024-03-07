from flask import Flask, request, render_template

app = Flask(__name__) # Создание экземпляра класса

@app.route('/')
def index():
    return 'Введи путь к файлу в адресной строке'

# Get запрос
@app.get('/submit')
def submit_get():
    return render_template('form.html')

# POST запрос
@app.post('/submit')
def submit_post():
    name = request.form.get('name')
    return f'Hello {name}!'

if __name__ == '__main__':
    app.run()

