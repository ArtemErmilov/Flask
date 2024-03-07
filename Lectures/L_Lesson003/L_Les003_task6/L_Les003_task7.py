from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect

from forms_2 import LoginForm, RegistrationForm

app = Flask(__name__) # Создание экземпляра класса

# Настройка защиты от CSRF-атак
app = Flask(__name__)
app.config['SECRET_KEY'] = b'6f55a245c6bd9a2ae4f321cdd22590e4b2137f246c3ea5d85dfe9460b63e5d92'
csrf = CSRFProtect(app)

@app.route('/')
def index():
    return 'Привет'

# Отображение форм на страницах приложения
@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
    # Обработка данных из формы
        pass
    return render_template('login.html', form=form)

# Обработка данных из формы (Регистрация данных)
@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        email = form.email.data
        password = form.password.data
        print(email, password)
        ...
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)