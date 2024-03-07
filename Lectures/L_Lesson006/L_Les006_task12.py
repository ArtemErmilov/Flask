from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., title="The ID of theitem"), q: str = None):
    return {"item_id": item_id, "q": q}