from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(max_length=10) # Имя может состоять максимум из 10 символов

class User(BaseModel):
    age: int = Field(default=0) # Если строка не будет заполнена, то в неё по умолчанию введётся 0