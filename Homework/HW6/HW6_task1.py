# ДЗ №6
# 📌 Необходимо создать базу данных для интернет-магазина. База данных должна
# состоять из трех таблиц: товары, заказы и пользователи. Таблица товары должна
# содержать информацию о доступных товарах, их описаниях и ценах. Таблица
# пользователи должна содержать информацию о зарегистрированных
# пользователях магазина. Таблица заказы должна содержать информацию о
# заказах, сделанных пользователями.
#     ○ Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY),
#     имя, фамилия, адрес электронной почты и пароль.
#     ○ Таблица товаров должна содержать следующие поля: id (PRIMARY KEY),
#     название, описание и цена.
#     ○ Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id
#     пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус
#     заказа.

# 📌 Создайте модели pydantic для получения новых данных и
# возврата существующих в БД для каждой из трёх таблиц
# (итого шесть моделей).

# 📌 Реализуйте CRUD операции для каждой из таблиц через
# создание маршрутов, REST API (итого 15 маршрутов).
#     ○ Чтение всех
#     ○ Чтение одного
#     ○ Запись
#     ○ Изменение
#     ○ Удаление

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime, timedelta
import random 

# Создание базы данных
DATABASE_URL = "sqlite:///Homework/HW6/instance/databaseHW6.db" 

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Создание таблиц

# Товары
products = sqlalchemy.Table( # Создание таблицы товары 
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer,
    primary_key=True),
    sqlalchemy.Column("product_name", sqlalchemy.String(128)),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("price", sqlalchemy.Float),
)

# Пользователи
users = sqlalchemy.Table( # Создание таблицы пользователи 
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer,
    primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("surname", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(32)),
)

# Заказы
orders = sqlalchemy.Table( # Создание таблицы заказы 
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer,
    primary_key=True),
    sqlalchemy.Column("id_user", sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column("id_products", sqlalchemy.Integer, sqlalchemy.ForeignKey('products.id')),
    sqlalchemy.Column("order_date", sqlalchemy.DateTime),
    sqlalchemy.Column("status", sqlalchemy.String(128)),
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
#{"check_same_thread": False} - используися для конекекта не асинхронного sqllit и sqlachemy

metadata.create_all(engine)

app = FastAPI()

class UserIn(BaseModel):
    name: str = Field(max_length=32)
    surname: str = Field(max_length=32)
    email: str = Field(max_length=128)
    password: str = Field(max_length=32)

class User(UserIn):
    id: int

@app.get("/in_users/{count}") # Автоматическое заполнение базы покупателями
async def create_users(count: int):
    for i in range(1,count+1):
        query = users.insert().values(name=f'Имя{i}', surname=f'Фамилия{i}', email=f'mail{i}@mail.ru', password=f'pass{i}')
        await database.execute(query)
    return {'message': f'Создано {count} пользователей.'}

class ProductsIn(BaseModel):
    product_name:str = Field(max_length=32)
    description:str = Field(max_length=1500)
    price:float = Field()

class Products(ProductsIn):
    id: int

@app.get("/in_products/{count}") # Автоматическое заполнение базы товарами
async def create_products(count: int):
    for i in range(1,count+1):
        query = products.insert().values(product_name=f'Название товара{i}', description=f'Описание товара{i}', price=random.uniform(1000,100_000))
        await database.execute(query)
    return {'message': f'Создано {count} товаров в базе данных.'}

class OrdersIn(BaseModel):
    id_user:int = Field()
    id_products:int = Field()
    order_date:datetime = Field()
    status:str = Field(max_length=128)

class Orders(OrdersIn):
    id: int

@app.get("/in_orders/{count}") # Автоматическое заполнение базы заказами
async def create_orders(count: int):
    status_list = ['В обработке.', 'В доставке.', 'В пункте выдачи.','Забран покупателем.']
    query_users = users.select()
    qu = await database.fetch_all(query_users)
    query_products = products.select()
    qp = await database.fetch_all(query_products)
    list_id_us = []
    list_id_prod = []
    for us in qu:
       list_id_us.append(us[0])
    for pr in qp:
       list_id_prod.append(pr[0])
    for i in range(1,count+1):
        query = orders.insert().values(id_user=random.choice(list_id_us), id_products = random.choice(list_id_prod), order_date = datetime.utcnow() - timedelta(hours= (count-i), minutes=random.randint(1,60)), status = random.choice(status_list))
        await database.execute(query) # order_date = datetime.utcnow(),
     
    return {'message': f'Создано {count} заказов.'}


# Внесение данных по пользователям
# Чтение пользователей из БД, read. Чтение всех пользователей и вывод их в виде jsone файла. 
@app.get("/users/read_user/", response_model=List[User])
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
    query = users.insert().values(name=user.name, surname=user.surname, email=user.email,password=user.password)
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

# Внесение данных по товарам

# Чтение перечня товаров из БД, read. 
@app.get("/product/read_products/", response_model=List[Products])
async def read_products():
    query = products.select() #Выбор всех товаров из списка. 
    return await database.fetch_all(query)# Вывод всех данных

# Чтение одного товара из БД по ID, read и вывод его данных 
@app.get("/product/read_product/{product_id}", response_model=Products)
async def read_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query) # Вывод данных одного товара

# Создание нового товар в БД, create
@app.post("/product/create/", response_model=Products)# response_model=Products
async def create_product_new(product: ProductsIn):
    query = products.insert().values(product_name=product.product_name, description=product.description, price=product.price)
    last_record_id = await database.execute(query) 
    return {**product.model_dump(), "id": last_record_id }

# Обновление данных по товарам в БД по ID, update
@app.put("/product/update/{product_id}", response_model=Products)
async def update_product(product_id: int, new_product: ProductsIn):
    query = products.update().where(products.c.id == product_id).values(**new_product.dict())# update - обновление данных, where - поиск пользователя по ID, values - обновление данных в базе данных 
    await database.execute(query)
    return {**new_product.dict(), "id": product_id}

# Удаление продукта из БД по ID, delete
@app.delete("/product/delete/{product_id}")
async def delete_product(product_id: int):
    query = products.delete().where( products.c.id ==  product_id)
    await database.execute(query)
    return {'message': 'Продукт удалён.'}



# Внесение данных по заказам

# Чтение перечня заказов из БД, read. 
@app.get("/orders/read_orders/", response_model=List[Orders])
async def read_orders():
    query = orders.select() #Выбор всех товаров из списка. 
    return await database.fetch_all(query)# Вывод всех данных

# Чтение одного заказа из БД по ID, read и вывод его данных 
@app.get("/orders/read_order/{product_id}", response_model=Orders)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query) # Вывод данных одного товара


# Удаление заказа из БД по ID, delete
@app.delete("/orders/delete/{product_id}")
async def delete_orders(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': 'Заказ удалён.'}


# Создание нового заказа в БД, create
@app.post("/orders/create/")# response_model=Orders
async def create_orders_new(order: OrdersIn):
    query_user = users.select().where(users.c.id == order.id_user)
    dat_user = await database.fetch_one(query_user) 
    query_prod = products.select().where(products.c.id == order.id_products)
    dat_prod = await database.fetch_one(query_prod) 
    if (not dat_user ):
        return {'message': f'Пользователя с ID {order.id_user} не существует!'} 
    elif (not dat_prod):
         return {'message': f'Товара с ID {order.id_products} не существует!'} 
    query =  orders.insert().values(id_user=order.id_user, id_products=order.id_products, order_date=order.order_date, status=order.status)
    last_record_id = await database.execute(query) 
    return {**order.model_dump(), "id": last_record_id } 


# Обновление данных по заказу в БД по ID, update
@app.put("/orders/update/{orders_id}")# response_model=Products
async def update_orders(order_id: int, new_order: OrdersIn):
    query_user = users.select().where(users.c.id == new_order.id_user)
    dat_user = await database.fetch_one(query_user) 
    query_prod = products.select().where(products.c.id == new_order.id_products)
    dat_prod = await database.fetch_one(query_prod) 
    if (not dat_user ):
        return {'message': f'Пользователя с ID {new_order.id_user} не существует!'} 
    elif (not dat_prod):
         return {'message': f'Товара с ID {new_order.id_products} не существует!'} 
    query = orders.update().where(orders.c.id == order_id).values(**new_order.dict())# update - обновление данных, where - поиск пользователя по ID, values - обновление данных в базе данных 
    await database.execute(query)
    return {**new_order.dict(), "id": order_id}


# uvicorn Homework.HW6.HW6_task1:app --reload