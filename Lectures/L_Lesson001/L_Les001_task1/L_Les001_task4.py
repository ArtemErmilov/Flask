from flask import Flask 

app = Flask(__name__) # Создание экземпляра класса

@app.route('/Фёдор/')
@app.route('/Fedor/')
@app.route('/Федя/')
def fedor():
    return 'Привет, Феодор!'

if __name__ == '__main__':
    app.run(debug=True)