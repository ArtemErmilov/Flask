from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length

# Логин и пароль
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()]) # ПОле для ввода имени пользователя.
    password = PasswordField('Password', validators=[DataRequired()]) # Поле для ввода пароля.

# Регистрация данных
class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()]) # StringField - строкавое поле, validators=[DataRequired()] - обязательный ввод данных.
    age = IntegerField('Age', validators=[DataRequired()]) # IntegerField - поле со значением целочисленным. обязательный ввод
    gender = SelectField('Gender', choices=[('male', 'Мужчина'),('female', 'Женщина')]) # Поле с выбором пола.
# Валидация данных формы (ввод регистрационных данных)
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()]) # Поле ввода логина в виде Email
    password = PasswordField('Password', validators=[DataRequired(), Length (min=6)]) # Поле ввода пароля
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo  ('password')]) # Поле ввода пароля для проверки.