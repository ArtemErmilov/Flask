from flask import Flask 

app = Flask(__name__) # Создание экземпляра класса

@app.route('/')
def index():
    return 'Привет, незнакомец!'

@app.route('/text/')
def text():
    return """<p>Вот не думал, не гадал,<br>Программистом взял и
                стал.<br>Хитрый знает он язык,<br>Он к другому не привык.</p>"""

if __name__ == '__main__':
    app.run(debug=True)