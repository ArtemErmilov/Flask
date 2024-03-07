# Задание №2

# Создать страницу, на которой будет изображение и ссылка
# на другую страницу, на которой будет отображаться форма
# для загрузки изображений.

from pathlib import PurePath, Path
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__) # Создание экземпляра класса


@app.route('/') # Декорирование функции
def hello_world(): # Запускаемая функция при обращение к сайту
    return 'Hello World!'

@app.route('/first', methods=['GET', 'POST'])# Загрузка файла через html 
def first_page(): 
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'Practice/P_Lesson002/P_Les002_task2/uploads',file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template('first.html')


@app.route('/next/') 
def next_page(): 
    return render_template('next.html')

if __name__ == '__main__':
    app.run(debug=True)