from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str # Обязательное заполнение
    description: Optional[str] = None # Не обязательное заполнение
    price: float # Обязательное заполнение
    tax: Optional[float] = None # Не обязательное заполнение