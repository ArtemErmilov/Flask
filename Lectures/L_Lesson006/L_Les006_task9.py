import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field



DATABASE_URL = "sqlite:///Lectures/L_Lesson006/instance/mydatabase.db" # Создание базы данных в корневой директории

database = databases.Database(DATABASE_URL) # Создание движка для базы данных.
metadata = sqlalchemy.MetaData()

# Заполнение базы данных таблицами с полями

users = sqlalchemy.Table( # Создание таблицы в базе данных
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer,
    primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)

app = FastAPI()

class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)

class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)

# Создание пользователя в БД, create
@app.post("/users/create/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(name=user.name,email=user.email)
    # query = users.insert().values(**user.dict())# Тоже самое что старкой выше
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}

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

# Обновление пользователя в БД по ID, update
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
    return {'message': 'User deleted'}