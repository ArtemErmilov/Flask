# Метод GET
import logging
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def read_root():
    # logger.info("Отработал GET запрос.")
    return {"Hello": "World"}

#  uvicorn Lectures.L_Lesson005.L_Les005_task1.L_Les005_task3:app --reload - Старт сервер
