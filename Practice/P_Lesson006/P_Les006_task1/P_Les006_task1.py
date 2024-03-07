# Задание 1

#  Разработать API для управления списком пользователей с
# использованием базы данных SQLite. Для этого создайте
# модель User со следующими полями:
#     ○ id: int (идентификатор пользователя, генерируется
#     автоматически)
#     ○ username: str (имя пользователя)
#     ○ email: str (электронная почта пользователя)
#     ○ password: str (пароль пользователя)

# API должно поддерживать следующие операции:

#       ○ Получение списка всех пользователей: GET /users/
#       ○ Получение информации о конкретном пользователе: GET /users/{user_id}/
#       ○ Создание нового пользователя: POST /users/
#       ○ Обновление информации о пользователе: PUT /users/{user_id}/
#       ○ Удаление пользователя: DELETE /users/{user_id}/
# 📌 Для валидации данных используйте параметры Field модели User.
# 📌 Для работы с базой данных используйте SQLAlchemy и модуль databases.

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field


DATABASE_URL = "sqlite:///Practice/P_Lesson006/P_Les006_task1/instance/mydatabase.db" # Создание базы данных в корневой директории - адрес базы данных

database = databases.Database(DATABASE_URL) # Создание базы данных
metadata = sqlalchemy.MetaData()

# Заполнение базы данных таблицами с полями

users = sqlalchemy.Table( # Создание таблицы в базе данных
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer,
    primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(32)),
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
#{"check_same_thread": False} - используися для конекекта не асинхронного sqllit и sqlachemy

metadata.create_all(engine)

app = FastAPI()

class UserIn(BaseModel):
    username: str = Field(max_length=32)
    email: str = Field(max_length=128)
    password: str = Field(max_length=32)

class User(BaseModel):
    id: int
    username: str = Field(max_length=32)
    email: str = Field(max_length=128)
    password: str = Field(max_length=32)

# @app.get("/fake_users/{count}")
# async def create_note(count: int):
#     for i in range(1,count):
#         query = users.insert().values(username=f'name{i}',email=f'mail{i}@mail.ru',password=f'pass{i}')
#         await database.execute(query)
#     return {'message': f'{count} fake users create'}


from typing import List 
# Чтение пользователей из БД, read. Чтение всех пользователей и вывод их в виде jsone файла. 
@app.get("/users/read_users/", response_model=List[User])
async def read_users():
    query = users.select() #Выбор всех пользователей из списка. 
    return await database.fetch_all(query)# Вывод всех данных

# Чтение одного пользователя из БД по ID, read и вывод его данных 
@app.get("/users/read_user/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query) # Вывод данных одного пользователя

# Создание пользователя в БД, create
@app.post("/users/create/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(username=user.username,email=user.email,password=user.password)
    last_record_id = await database.execute(query) # last_record_id =
    return {**user.model_dump(), "id": last_record_id }# "id": last_record_id


# Обновление данных пользователя в БД по ID, update
@app.put("/users/update/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())# update - обновление данных, where - поиск пользователя по ID, values - обновление данных в базе данных 
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}

# Удаление пользователя из БД по ID, delete
@app.delete("/users/delete/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'Пользователь удалён.'}


# uvicorn Practice.P_Lesson006.P_Les006_task1.P_Les006_task1:app --reload
