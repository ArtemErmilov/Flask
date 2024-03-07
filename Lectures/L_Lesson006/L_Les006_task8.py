import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field 


DATABASE_URL = "sqlite:///Lectures/L_Lesson006/instance/mydatabase.db" # Создание базы данных в корневой директории

database = databases.Database(DATABASE_URL) # Создание движка для базы данных.
metadata = sqlalchemy.MetaData()

# Заполнение базы данных таблицами с полями

users = sqlalchemy.Table(
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

@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(name=f'user{i}',email=f'mail{i}@mail.ru')
        await database.execute(query)
    return {'message': f'{count} fake users create'}