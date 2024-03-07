# Создание модуля
from fastapi import FastAPI

app = FastAPI() 

# Настройка сервера и маршрутизации
@app.get("/")
async def root():
    return {"Hello": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

