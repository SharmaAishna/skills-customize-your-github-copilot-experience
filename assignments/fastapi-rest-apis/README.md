# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API in Python using FastAPI to manage tasks and practice creating endpoints, request models, and validation. By the end of this assignment, students will understand how to expose JSON data through a web API and test it with interactive docs.

## 📝 Tasks

### 🛠️ Create the FastAPI App

#### Description
Set up a new FastAPI application and create a simple root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import and initialize `FastAPI`.
- Create an app instance with a title such as `Task API`.
- Add a `GET /` endpoint that returns a JSON message like `"Welcome to the Task API!"`.
- Start the API locally with Uvicorn or another ASGI server.

### 🛠️ Build a Task Resource

#### Description
Create endpoints for listing tasks and adding a new task to an in-memory list.

#### Requirements
Completed program should:

- Store tasks in a Python list or dictionary.
- Add a `GET /tasks` endpoint that returns all tasks as JSON.
- Add a `POST /tasks` endpoint that accepts task data and creates a new item.
- Return task data with fields such as `id`, `title`, and `done`.
- Ensure new tasks are added to the in-memory collection.

### 🛠️ Add Validation and Detail Endpoints

#### Description
Improve the API by validating inputs and creating endpoints for retrieving or updating an individual task.

#### Requirements
Completed program should:

- Use `pydantic` models to validate request data.
- Require a meaningful task title and allow a boolean `done` status.
- Add a `GET /tasks/{task_id}` endpoint to return a single task.
- Add a `PUT /tasks/{task_id}` endpoint to update an existing task.
- Return a `404` error when a task ID does not exist.
- Use FastAPI's automatic interactive docs by visiting `/docs`.

