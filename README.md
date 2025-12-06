# Custom Resume Builder

A Django-based web application that helps users create professional resumes using various templates.

## Features

- **User Authentication**: Secure Sign Up and Sign In functionality.
- **Multiple Templates**: Choose from Professional, Simple, or Creative resume templates.
- **Interactive Form**: Easy-to-use form to input personal details, education, experience, skills, and more.
- **Resume Management**: Dashboard to view, edit, and manage your resumes.
- **Admin Dashboard**: Special dashboard for administrators to view user stats.
- **PDF Export**: (Implicit support via browser print/save as PDF).

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/d-hackmt/custom_resume_builder_django.git
    cd Custom-Resume-Builder
    ```

2.  **Create and activate a virtual environment (Recommended):**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Database Setup

1.  **Run Migrations:**
    Initialize the database by running the following command:
    ```bash
    python manage.py migrate
    ```

2.  **Create a Superuser (Optional):**
    You can create an admin account to access the admin dashboard.
    
    A utility script is provided to quickly create a default admin user (`admin`/`admin`):
    ```bash
    python create_superuser.py
    ```
    
    Or use the standard Django command:
    ```bash
    python manage.py createsuperuser
    ```

## Running the Application

1.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

2.  **Access the application:**
    Open your web browser and navigate to:
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Project Structure

- `core/`: Main application logic (models, views, forms).
- `resume_builder/`: Project settings and configuration.
- `templates/`: HTML templates for the frontend.
- `static/`: CSS, JavaScript, and images.
- `manage.py`: Django's command-line utility.

## Usage

1.  **Sign Up**: Create a new account.
2.  **Dashboard**: After logging in, you will be redirected to the dashboard where you can see available templates.
3.  **Create Resume**: Click "Edit Form" or select a template to start filling in your details.
4.  **View/Print**: Once filled, view your resume in your chosen template. You can save the page as PDF (Ctrl+P -> Save as PDF) to export it.

## Troubleshooting

-   **Database Errors**: If you encounter database errors, try deleting `db.sqlite3` and running `python manage.py migrate` again.
-   **Static Files**: If images are not loading, ensure `DEBUG` is set to `True` in `settings.py` for development.
