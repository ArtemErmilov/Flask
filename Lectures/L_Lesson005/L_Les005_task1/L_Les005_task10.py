from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
    
# для получение 2го ретёрна надо ввести http://127.0.0.1:8000/items/42?q=245784451