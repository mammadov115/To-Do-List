## 📝 To-Do List API (Django + DRF)

A powerful and clean **CRUD-based To-Do List REST API** built with Django and Django REST Framework. It supports **user authentication (JWT)**, **filtering**, **searching**, and **ordering** of tasks.

---

### 🚀 Features

* ✅ Token-based user authentication (JWT)
* ✅ User registration and login
* ✅ Create / Read / Update / Delete To-Do items
* ✅ Filter tasks by `is_completed` or `title`
* ✅ Search tasks by keyword in `title` or `description`
* ✅ Order tasks by `created_at` or `updated_at`
* ✅ Only authenticated users can manage their own tasks

---

### 🛠️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/mammadov115/todo-api.git
cd todo-api
```

2. **Create virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run migrations:**

```bash
python manage.py migrate
```

5. **Create a superuser (optional):**

```bash
python manage.py createsuperuser
```

6. **Run the development server:**

```bash
python manage.py runserver
```

---

### 🔐 Authentication

The project uses **JWT authentication**.

* **Register:** `POST /api/register/`
* **Login:** `POST /api/token/` → Returns `access` and `refresh` tokens
* Use the token in the header:

```http
Authorization: Bearer <access_token>
```

---

### 📌 API Endpoints

| Method | Endpoint           | Description             |
| ------ | ------------------ | ----------------------- |
| POST   | `/api/register/`   | Register new user       |
| POST   | `/api/token/`      | Login and get JWT token |
| GET    | `/api/todos/`      | List all your tasks     |
| POST   | `/api/todos/`      | Create new task         |
| GET    | `/api/todos/<id>/` | Retrieve single task    |
| PUT    | `/api/todos/<id>/` | Update task             |
| DELETE | `/api/todos/<id>/` | Delete task             |

---

### 🔍 Filtering, Searching, Ordering

You can enhance your task query with:

* **Filtering:**

  * `/api/todos/?is_completed=true`
  * `/api/todos/?title=Buy`

* **Searching:**

  * `/api/todos/?search=groceries`

* **Ordering:**

  * `/api/todos/?ordering=created_at`
  * `/api/todos/?ordering=-updated_at`

---

### ✅ Running Tests

Tests are written with **pytest** and **DRF test client**.

```bash
pytest
```

---

### 📦 Technologies Used

* Python
* Django
* Django REST Framework
* Simple JWT
* Pytest
* SQLite/PostgreSQL

---

### 👨‍💻 Author

Made with ❤️ by 
[**Mehman Mammadov**](https://github.com/mammadov115)

---

### 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more info.

