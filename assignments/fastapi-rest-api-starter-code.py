from fastapi import FastAPI

app = FastAPI(title="Item API")

items = [
    {"id": 1, "name": "Sample Item", "price": 9.99},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI API!"}


# TODO: Add CRUD routes for managing items


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
