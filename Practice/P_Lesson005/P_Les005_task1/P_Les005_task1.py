# Задание №1
# 📌 Создать API для управления списком задач. Приложение должно иметь
# возможность создавать, обновлять, удалять и получать список задач.
# 📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
# 📌 Создайте класс Task с полями id, title, description и status.
# 📌 Создайте список tasks для хранения задач.
# 📌 Создайте маршрут для получения списка задач (метод GET).
# 📌 Создайте маршрут для создания новой задачи (метод POST).
# 📌 Создайте маршрут для обновления задачи (метод PUT).
# 📌 Создайте маршрут для удаления задачи (метод DELETE).
# 📌 Реализуйте валидацию данных запроса и ответа.

import logging
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from typing import Optional,Any, List, Union
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str
    status : str 

tasks = []

@app.get("/")
async def read_root(): # GET запрос
    logger.info("Отработал GET запрос.")
    return {"Hello": "World"}

@app.get("/gettask/", response_model=List[Task])
async def read_task(): # GET запрос
    for dt in tasks:
        print (dt)
    logger.info("\nОтработал GET запрос. gettask")
    return tasks

@app.get("/gettask/{task_id}", response_model=Task)
async def read_task(task_id:int): # GET запрос
    for dat in tasks:
        if dat.id == task_id:
            logger.info("\nОтработал GET запрос.")
            return dat
    return HTTPException(status_code=404, detail="Такого ID нет")

@app.post("/posttask/", response_model=Task)
async def reate_task(task:Task):# POST запрос
    logger.info('Отработал POST запрос.')
    tasks.append (task)
    return task

@app.put("/puttask/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task): # PUT запрос
    for i, dat in enumerate(tasks):
        if dat.id == task_id:
            tasks[i] = task
            print(dat)
            logger.info(f'Отработал PUT запрос для task_id = {task_id}.')
            for d in tasks:
                print(d)
            return dat
    return HTTPException(status_code=404, detail='Такого ID нет')

@app.delete("/deletetask/{task_id}")
async def delete_task(task_id: int): # DELETE запрос
    for dat in tasks:
        if dat.id == task_id:
            tasks.remove(dat)
            logger.info(f'Отработал DELETE запрос для item id = {task_id}.')
            # return {"item_id": item_id}
            return dat
    return HTTPException(status_code=404, detail='Такого ID нет')

def add_tasks(tasks: list, num:int):

    return