from flask import Flask, request, render_template

app = Flask(__name__) # Создание экземпляра класса

@app.route('/')
def index():
    return 'Введи путь к файлу в адресной строке'

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'
    return render_template('form.html')

if __name__ == '__main__':
    app.run()

