# 📝 Task Manager API

A simple **Task Manager** built with **Django REST Framework** that allows users to register, log in, and manage their tasks efficiently.

---

## 🚀 Features
- User Registration & Login
- JWT Token Authentication
- Create, Read, Update & Delete (CRUD) tasks
- Mark tasks as complete
- Admin panel for user management

---

## 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** SQLite
- **Authentication:** Token Authentication
- **Hosting:** (optional - e.g., Render / Railway)

---

## 📦 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/Mariam3649/task-manager.git
   cd task-manager
## 🔑 API Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | /api/register/ | Register new user |
| POST | /api/login/ | Login user and get token |
| GET | /api/tasks/ | List user’s tasks |
| POST | /api/tasks/ | Create new task |
| PUT | /api/tasks/<id>/ | Update a task |
| DELETE | /api/tasks/<id>/ | Delete a task |
| PATCH | /api/tasks/<id>/complete/ | Mark task as completed |

   
