from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Item API")


class ItemInput(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)


items: dict[int, dict[str, object]] = {
    1: {"id": 1, "name": "Sample Item", "price": 9.99}
}
next_item_id = 2


@app.get("/")
def read_root():
    return {"message": "Welcome to the Item API!"}


# TODO: Add GET /items and GET /items/{item_id} routes.
# TODO: Add POST /items, PUT /items/{item_id}, and DELETE /items/{item_id} routes.
