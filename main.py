from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="My FastAPI Project", version="1.0.0")

class Item(BaseModel):
    name: str
    description: str = None
    price: float

@app.get("/")
async def root():
    return {"message": "Welcome to My FastAPI Project!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
async def create_item(item: Item):
    return {"item": item, "message": "Item created successfully"}