from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()]) # ПОле для ввода имени пользователя.
    password = PasswordField('Password', validators=[DataRequired()]) # Поле для ввода пароля.