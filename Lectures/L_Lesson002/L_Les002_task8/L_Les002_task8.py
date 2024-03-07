from pathlib import PurePath, Path
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'Lectures/L_Lesson002/L_Les002_task8/uploads',file_name))
        # 'Lectures/L_Lesson002/L_Les002_task8/uploads' - Папка для загрузки файла
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html')

if __name__ == '__main__':
    app.run()

