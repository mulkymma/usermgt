# Django User Management System

This project is a Django-based user management system that provides custom user registration, email verification, and profile management. It is designed for easy extension and integration into larger Django projects.

---

## Technologies Used

- **Python 3.x**: The core programming language.
- **Django**: The main web framework for rapid development and clean, pragmatic design.
- **SQLite**: Default database for development (via `db.sqlite3`).
- **Django Admin**: For managing users and other models.
- **Django Custom User Model**: Allows for flexible user attributes and authentication.
- **Django Forms**: For user registration and profile updates.
- **Django Email Backend (Console)**: Prints verification emails to the console for development/testing.
- **HTML Templates**: For user-facing pages (registration, profile).

---

## Project Structure

```
db.sqlite3
manage.py
README.md
accounts/
    admin.py
    apps.py
    forms.py
    models.py
    tests.py
    urls.py
    views.py
    migrations/
    templates/
        profile.html
        register.html
user_mgmt/
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py
```

---

## Features

- **Custom User Model**: Located in `accounts/models.py` for flexibility.
- **User Registration**: With email verification (link sent to console).
- **Profile Management**: Users can update their profile.
- **Admin Integration**: Manage users via Django admin.
- **Email Verification**: Ensures only verified users can log in.

---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd mma
```

### 2. Create a Virtual Environment (Recommended)

```sh
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```sh
pip install django
```

### 4. Apply Migrations

```sh
python manage.py migrate
```

### 5. Create a Superuser (Optional)

```sh
python manage.py createsuperuser
```

### 6. Run the Development Server

```sh
python manage.py runserver
```

### 7. Access the Application

- Home: [http://localhost:8000/](http://localhost:8000/)
- Register: [http://localhost:8000/register/](http://localhost:8000/register/)
- Profile: [http://localhost:8000/profile/](http://localhost:8000/profile/)
- Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## Email Verification
username:mulkymma
password:mulky12345
- After registration, a verification link is printed to the console.
- Copy and paste the link into your browser to activate your account.

---

## Customization

- **User Model**: [`accounts.models.CustomUser`](accounts/models.py)
- **Forms**: [`accounts.forms`](accounts/forms.py)
- **Views**: [`accounts.views`](accounts/views.py)
- **URLs**: [`user_mgmt.urls`](user_mgmt/urls.py), [`accounts.urls`](accounts/urls.py)



## Contributing

Feel free to fork this repository and submit pull requests!

---

## Troubleshooting

- Ensure you are using Python 3.x.
- If you encounter issues with migrations, try deleting the `db.sqlite3` file and the `migrations/` folders (except `__init__.py`), then re-run migrations.
- For email verification in production, configure Django's email backend in `settings.py`.
