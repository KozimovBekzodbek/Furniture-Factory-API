# 🪑 Furniture Factory API

A complete RESTful API built with Django and Django REST Framework to manage a furniture manufacturing process — from raw materials to finished products. Ideal for small and medium-sized furniture workshops.

---

## 🚀 Features

* ✅ JWT Authentication (via SimpleJWT)
* ✅ Manage Orders with detailed statuses (New, In Progress, Ready)
* ✅ Assign Workers with roles and tasks
* ✅ Manage Raw Materials with stock tracking and images
* ✅ Finished Products are generated from completed Orders
* ✅ Admin panel optimized for production workflow
* ✅ Powerful filtering via query parameters (status, type, etc.)

---

## 🧱 Technologies Used

* Python 3.10+
* Django 4.x
* Django REST Framework
* SimpleJWT (Authentication)
* django-resized (Image resizing)
* SQLite (can switch to PostgreSQL)

---

## 🔐 Authentication

This API uses **JWT authentication**.

**Obtain Token:**

```http
POST /api/token/
{
  "username": "admin",
  "password": "admin"
}
```

Include the access token in all requests:

```
Authorization: Bearer <your-access-token>
```

---

## 📦 API Endpoints Overview

| Resource          | Endpoint              | Methods                |
| ----------------- | --------------------- | ---------------------- |
| Orders            | `/orders/`            | GET, POST, PUT, DELETE |
| Workers           | `/workers/`           | GET, POST, PUT, DELETE |
| Customers         | `/customers/`         | GET, POST, PUT, DELETE |
| Raw Materials     | `/raw-materials/`     | GET, POST, PUT, DELETE |
| Finished Products | `/finished-products/` | GET, POST, PUT, DELETE |

**Filter Orders by Status:**

```http
GET /orders/?status=Ready
```

---

## 📊 Workflow (Recommended Order)

1. Add Raw Materials
2. Add Workers
3. Add Customers
4. Create an Order (mark as `Ready` when completed)
5. Create a Finished Product from a Ready Order
6. Track product stock and worker contributions

---

## 🖼️ Admin Panel

The Django admin panel is optimized:

* Inline editing of Order Workers
* Only Ready Orders shown when creating Finished Product
* Material and Product images managed easily

Run:

```bash
python manage.py createsuperuser
```

---

## ⚙️ Setup Instructions

1. Clone the repo:

```bash
git clone https://github.com/yourusername/Furniture-Factory-API.git
cd fFurniture-Factory-API
```

2. Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Run server:

```bash
python manage.py runserver
```

---

## 📆 Postman Testing

* Use `/api/token/` to get access
* Use endpoints listed above for CRUD
* Upload images using `form-data`
* Filter orders by status: `/orders/?status=Ready`

---

## 🔧 Future Improvements

* Deduct raw material quantity after order completion
* PDF invoices for finished products
* Order-based production dashboard
* Frontend interface with React/Vue

---


##  Contact

Telegram: [@yourhandle](https://t.me/kozimov_01)
