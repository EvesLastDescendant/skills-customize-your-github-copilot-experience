# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a small REST API with FastAPI by creating endpoints, using request and response models, and handling basic CRUD operations for a collection of items.

## 📝 Tasks

### 🛠️ Create the FastAPI App

#### Description
Set up a FastAPI application and verify that it runs locally.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance
- Add a `/health` endpoint that returns a simple JSON response
- Run the app with Uvicorn and confirm the server responds successfully

### 🛠️ Add a Resource Model and Create/List Endpoints

#### Description
Build endpoints to manage a simple resource such as tasks or books.

#### Requirements
Completed program should:

- Define a Pydantic model for the resource
- Store items in an in-memory list
- Add a `GET /items` endpoint to return all items
- Add a `POST /items` endpoint to create a new item and return it

### 🛠️ Add Validation and Detail Endpoints

#### Description
Expand the API with validation and item-specific routes.

#### Requirements
Completed program should:

- Validate required fields such as title and description
- Add a `GET /items/{item_id}` endpoint to return one item
- Add a `PUT` or `DELETE` endpoint for updating or removing an item
- Return clear JSON responses for success and not-found cases
