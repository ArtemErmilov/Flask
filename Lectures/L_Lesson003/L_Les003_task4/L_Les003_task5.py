from flask import Flask, render_template

from models_05 import db, User, Post


app = Flask(__name__) # Создание экземпляра класса

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db' # Подключение БД
db.init_app(app)

@app.route('/')
def index():
    return 'Привет'

@app.route('/data/')
def data():
    return 'Твои данные!'

# Получение данных из базы данных 
@app.route('/users/')
def all_users():
    users = User.query.all() #
    context = {'users': users}
    return render_template('users.html', **context)

# Фильтрация данных
@app.route('/users/<username>/')
def users_by_username(username):
    users = User.query.filter(User.username == username).all() # query - создание запроса, filter - создание фильтра по username, all - получение всех пользователей.
    context = {'users': users} # Данные всех пользователей переходят в context
    return render_template('users.html', **context)

#  Фильтрация по данным пользователя
from flask import jsonify
@app.route('/posts/author/<int:user_id>/')
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify([{'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'}), 404

# Фильтрация по времени
from datetime import datetime, timedelta
@app.route('/posts/last-week/')
def get_posts_last_week():
    date = datetime.utcnow() - timedelta(days=7) # От текущего времени отнимаем 7 дней и получаем дату, с которой начинается поиск
    posts = Post.query.filter(Post.created_at >= date).all() # Происходит фильтрация данных по дате которая больше или равно полученной date
    if posts:
        return jsonify([{'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at} for post in posts]) # Формирует данные по параметрам поиска в файл jsone
    else:
        return jsonify({'error': 'Posts not found'})

if __name__ == '__main__':
    app.run(debug=True)