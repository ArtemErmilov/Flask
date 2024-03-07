import logging
from fastapi import FastAPI

from typing import Optional
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class Item(BaseModel):
    name: str # Обязательное заполнение
    description: Optional[str] = None # Не обязательное заполнение
    price: float # Обязательное заполнение
    tax: Optional[float] = None # Не обязательное заполнение

app = FastAPI()

@app.get("/")
async def read_root(): # GET запрос
    logger.info("Отработал GET запрос.")
    return {"Hello": "World"}

@app.post("/items/")
async def create_item(item: Item):# POST запрос
    logger.info('Отработал POST запрос.')
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item): # PUT запрос
    logger.info(f'Отработал PUT запрос для item id = {item_id}.')
    return {"item_id": item_id, "item": item}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int): # DELETE запрос
    logger.info(f'Отработал DELETE запрос для item id = {item_id}.')
    return {"item_id": item_id}
