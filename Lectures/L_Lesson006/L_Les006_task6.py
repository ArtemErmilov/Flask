import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel 

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

