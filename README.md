# Django User Management System

A Django-based user management system featuring custom user registration, email verification, profile management (with profile picture upload), and a modern dashboard. Designed for easy extension and integration into larger Django projects.

---

## Technologies Used

- **Python 3.13.5**: Core programming language for backend logic.
- **Django 5.2.3**: Web framework for rapid development and clean design.
- **SQLite**: Default lightweight database for development.
- **Django Admin**: Built-in admin interface for managing users and models.
- **Custom User Model**: Flexible user attributes and authentication (`accounts/models.py`).
- **Django Forms**: For user registration and profile updates.
- **Django Email Backend (Console)**: Prints verification emails to the console for development/testing.
- **HTML Templates**: For user-facing pages (registration, profile, dashboard).
- **Branching**: The main branch is called `master`.

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
        base.html
        home.html
        register.html
        login.html
        profile.html
        dashboard.html
user_mgmt/
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py
images/
    register.png
    profile.png
    admin.png
```

---

## Features

- **Custom User Model**: Located in `accounts/models.py` for flexibility.
- **User Registration**: With email verification (link sent to console).
- **Profile Management**: Users can update their profile and upload a profile picture.
- **Dashboard**: Modern dashboard showing user info and verification status after login.
- **Admin Integration**: Manage users via Django admin.
- **Email Verification**: Ensures only verified users can log in.
- **Responsive & Clean UI**: Modern, mobile-friendly design.
- **Navigation Highlighting**: Current page is highlighted in the navigation bar.

---

## Updates / What’s New

- **Profile Picture Upload:**  
  Users can now upload and update their profile picture from the profile page. Uploaded images are stored in the `media/` directory and displayed on both the profile and dashboard pages.

- **Modern Dashboard:**  
  After login, users are redirected to a professional-looking dashboard that displays their username, email, profile picture (or avatar), and email verification status.

- **Improved Navigation:**  
  The navigation bar highlights the current page for better user experience.

- **Bug Fixes:**  
  - Fixed template inheritance issues (`extends`).
  - Corrected Django template syntax for navigation highlighting.
  - Improved error handling for user actions.

---

## Getting Started

### 1. Clone the Repository

```sh
git clone -b master <your-repo-url>
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
- Dashboard: [http://localhost:8000/dashboard/](http://localhost:8000/dashboard/)
- Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## Demo Login

You can use the following credentials to log in as a demo user:

- **Username:** `mulkymma`
- **Password:** `mulky12345`

---

## Email Verification

- After registration, a verification link is printed to the console.
- Copy and paste the link into your browser to activate your account.

---

## Customization

- **User Model**: [`accounts.models.CustomUser`](accounts/models.py)
- **Forms**: [`accounts.forms`](accounts/forms.py)
- **Views**: [`accounts.views`](accounts/views.py)
- **URLs**: [`user_mgmt.urls`](user_mgmt/urls.py), [`accounts.urls`](accounts/urls.py)

---

## Troubleshooting

- Ensure you are using Python 3.x.
- If you encounter issues with migrations, try deleting the `db.sqlite3` file and the `migrations/` folders (except `__init__.py`), then re-run migrations.
- For email verification in production, configure Django's email backend in `settings.py`.

---

## Contributing

- The main branch is called `master`.
- Feel free to fork this repository and submit pull requests!

