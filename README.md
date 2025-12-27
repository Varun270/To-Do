📝 To-Do List Web Application (FastAPI)

A web-based To-Do List application built using Python and FastAPI, providing RESTful APIs for managing tasks along with a template-based web interface.
The application uses raw SQL with SQLite (no ORM), implements centralized error handling, structured logging, and includes automated tests using pytest.

📌 Features

RESTful APIs for task management (CRUD)

Web interface using HTML templates (Jinja2)

SQLite database using raw SQL (no ORM)

Centralized exception handling

Application-level logging

Automated API testing with pytest

Auto-generated API documentation (Swagger / OpenAPI)

🛠️ Tech Stack
Component	Technology
Backend Framework	FastAPI
Language	Python 3.9+
Database	SQLite
Database Access	sqlite3 (Raw SQL)
Templating Engine	Jinja2
Testing	pytest
Server	Uvicorn

📂 Project Structure
```todo_app/
│
├── app/
│   ├── main.py              # Application entry point, APIs & exception handling
│   ├── database.py          # Database connection & initialization
│   ├── crud.py              # Raw SQL CRUD operations
│   ├── schema.py           # Pydantic models for request/response
│   ├── logging_config.py    # Logging configuration
│   ├── templates/           # HTML templates
│   │   ├── base.html
│   │   ├── tasks.html
│   │   └── add_task.html
│
├── tests/
│   └── tasks.py        # API test cases
│
├── requirements.txt
└── README.md
```

🧩 Database Design
Table: tasks
Column	Type	Description
id	INTEGER	Primary key (auto-increment)
title	TEXT	Task title (required)
description	TEXT	Task details
due_date	TEXT	Due date
status	TEXT	Task status (pending / done)

📌 Database is initialized automatically on application startup.

🔗 REST API Endpoints
➕ Create Task
POST /api/tasks


Request Body

{
  "title": "Buy groceries",
  "description": "Milk, Bread, Eggs",
  "due_date": "2025-01-10",
  "status": "pending"
}


Response

{
  "message": "Task created",
  "task_id": 1
}

📄 Get All Tasks
GET /api/tasks


Response

[
  {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, Bread, Eggs",
    "due_date": "2025-01-10",
    "status": "pending"
  }
]

🖥️ Web Interface (Templates)
Page	Description
/	Displays list of tasks
/add	Form to add a new task

Templates are rendered using Jinja2

HTML forms internally use API-backed logic

Clean separation between UI and API logic

⚠️ Error Handling

Centralized error handling is implemented in main.py using FastAPI exception handlers.

Covered Errors
Error Type	Handling
Validation errors	422 response with details
HTTP errors (404, 400)	Custom HTTPException handler
Database errors	SQLite exception handler
Unexpected errors	Global catch-all handler
Example
{
  "detail": "Internal Server Error"
}

📜 Logging

Application-level logging is enabled using Python’s logging module.

Logged Events

Application startup

API requests

Database operations

Validation failures

Runtime & unexpected errors

Sample Logs
INFO     API: Create task request - Buy groceries
INFO     DB: Task inserted with id=1
WARNING  Validation error at /api/tasks
ERROR    Database error at /api/tasks
CRITICAL Unhandled exception at /api/tasks

🧪 Testing

Automated tests are written using pytest.

Test Coverage - 

• Create task API

• Retrieve tasks API

• Response validation

Run Tests
pytest

📘 API Documentation

FastAPI provides automatic API documentation:

Swagger UI → http://localhost:8000/docs

OpenAPI JSON → http://localhost:8000/openapi.json

🚀 Setup & Run Instructions

1️⃣ Clone Repository

`git clone <your-repo-url>`

`cd todo_app`

2️⃣ Create Virtual Environment

`python -m venv venv`

`source venv/bin/activate   # Windows: venv\Scripts\activate`

3️⃣ Install Dependencies

`pip install -r requirements.txt`

4️⃣ Run Application

`uvicorn app.main:app --reload`

5️⃣ Open Browser

`http://localhost:8000`
