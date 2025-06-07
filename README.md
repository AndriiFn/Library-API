# Library Management System API

## Project Description

This project aims to **modernize** that experience by implementing a full-featured **online book borrowing system**. It will support managing books, users, borrowings, and payments through a **RESTful API** using **Django & Django REST Framework**, with Stripe integration for digital payments.

---

## Features

### Book Service
- Full CRUD support
- Fields:
  - `title`: `str`
  - `author`: `str`
  - `cover`: Enum: `HARD` | `SOFT`
  - `inventory`: positive `int`
  - `daily_fee`: `decimal ($USD)`
- Permissions:
  - Admin: Create/Update/Delete
  - Any User: View (List/Detail)

---

### Borrowing Service
- Features:
  - Borrow book (decrease inventory)
  - Return book (increase inventory)
  - Auto-assign borrowing to current user
  - Validates book availability

---

### Payment Service
- Integrated with Stripe
- Fields:
  - `status`: Enum: `PENDING` | `PAID`
  - `type`: Enum: `PAYMENT` | `FINE`
  - `borrowing_id`: `int`
  - `session_url`: `URL`
  - `session_id`: `str`
  - `money_to_pay`: `decimal ($USD)`
- Permissions:
  - Admins: Can view all payments
  - Users: Can view their own payments

---

## Tech Stack

- Python
- Django
- Django REST Framework
- JWT Authentication

---

## Running the Project

1. **Clone the repository**  
   ```bash
   git clone https://github.com/AndriiFn/library-API.git
   cd library-system
