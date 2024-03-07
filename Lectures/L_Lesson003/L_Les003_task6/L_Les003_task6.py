from flask import Flask, render_template
from flask_wtf import FlaskForm

app = Flask(__name__) # Создание экземпляра класса

# Настройка защиты от CSRF-атак 
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
app.config['SECRET_KEY'] = b'6f55a245c6bd9a2ae4f321cdd22590e4b2137f246c3ea5d85dfe9460b63e5d92'
csrf = CSRFProtect(app)

# генерация надёжного секретного ключа в терминале
# python 
# >>> import secrets 
# >>> secrets.token_hex()

@app.route('/')
def index():
    return 'Привет'

# Отключение защиты от CSRF атак
@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    return "Отключение защиты от CSRF атак"

if __name__ == '__main__':
    app.run(debug=True)