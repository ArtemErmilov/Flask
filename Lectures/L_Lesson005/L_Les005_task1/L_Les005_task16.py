from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
async def read_item(name: str, age: int):
    return {"Hello": name, "Age": age}