
from fastapi import FastAPI

app = FastAPI(title="FastApiLearning")


@app.get("/")
async def read_root():
    return {"message": "Hello FastAPI"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/name/{name}")
async def read_root(name: str):
    return {"message": f"Hello FastAPI {name}" }
