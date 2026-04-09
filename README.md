# ✅ Task Manager REST API

A RESTful API built with Flask and SQLAlchemy that allows users to create, read, update and delete tasks. Built as a demonstration of backend development skills including routing, database management, and HTTP methods.

## 🚀 Features

- Create, read, update and delete tasks (full CRUD)
- SQLite database with SQLAlchemy ORM
- JSON responses with proper HTTP status codes
- Input validation with error handling

## 🛠️ Tech Stack

- **Python 3**
- **Flask** — web framework and routing
- **Flask-SQLAlchemy** — database ORM
- **SQLite** — lightweight local database

## 📦 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/task-manager.git
cd task-manager
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python app.py
```

API will be running at `http://127.0.0.1:5000`

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/<id>` | Get a single task |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/<id>` | Update a task |
| DELETE | `/tasks/<id>` | Delete a task |

## 📝 Example Requests

**Create a task**
```json
POST /tasks
{
    "title": "Learn Flask",
    "description": "Build a REST API"
}
```

**Response**
```json
{
    "id": 1,
    "title": "Learn Flask",
    "description": "Build a REST API",
    "done": false
}
```

**Mark as done**
```json
PUT /tasks/1
{
    "done": true
}
```

## 📁 Project Structure

```
task-manager/
├── app.py             # Routes and app configuration
├── models.py          # Database models
├── requirements.txt   # Project dependencies
└── README.md
```

## 📦 Requirements

```bash
pip freeze > requirements.txt
```
