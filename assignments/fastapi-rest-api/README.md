# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI. You will create routes for working with items, validate request data with Pydantic, and use appropriate HTTP status codes.

## 📝 Tasks

### 🛠️ Set Up a FastAPI App

#### Description
Create and run a FastAPI application with a welcome route. Explore the interactive API documentation FastAPI generates for your app.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Add a `GET /` endpoint that returns a JSON welcome message
- Run the application locally with Uvicorn
- Open `/docs` and confirm the root endpoint is listed


### 🛠️ Create and Read Items

#### Description
Add endpoints for creating items and viewing the items stored in memory. Each item should have a unique ID, a name, and a price.

#### Requirements
Completed program should:

- Define a Pydantic request model requiring a non-empty `name` and a `price` greater than zero
- Add `POST /items` to create an item and return its assigned ID
- Add `GET /items` to return all items
- Add `GET /items/{item_id}` to return one item by ID
- Return `404 Not Found` when the requested item does not exist


### 🛠️ Update, Delete, and Validate Items

#### Description
Complete the item endpoints by adding update and delete operations. Try valid and invalid requests in `/docs` and observe the responses.

#### Requirements
Completed program should:

- Add `PUT /items/{item_id}` to replace an existing item's name and price
- Add `DELETE /items/{item_id}` to remove an existing item
- Return `404 Not Found` when an update or delete targets a missing item
- Return a success response after an item is deleted
- Let FastAPI reject invalid request data using the Pydantic model
