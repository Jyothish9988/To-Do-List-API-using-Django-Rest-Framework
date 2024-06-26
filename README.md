

# Todo App Installation Guide

This guide provides instructions for setting up the Todo app locally.
![Screenshot 1](screenshots/1.png)

![Screenshot 2](screenshots/2.png)

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.8 or higher)
- pip (Python package installer)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Jyothish9988/To-Do-List-API-using-Django-Rest-Framework.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd todo
   ```

3. **Create a Virtual Environment (Optional but Recommended):**

   ```bash
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment:**

   - **On Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **On macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies and Setup Database:**

   ```bash
   pip install django djangorestframework
   python manage.py migrate
   ```

   This will install the required Python packages (`Django` and `djangorestframework`) and set up the database.

6. **Create a Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create a superuser account. This account will allow you to access the Django admin interface.

## Running the Application

1. **Start the Django Development Server:**

   ```bash
   python manage.py runserver
   ```

2. **Access the Application:**

   Open a web browser and go to [http://127.0.0.1:8000/todos/api/](http://127.0.0.1:8000/todos/api/) to access the Todo app.

## Version Information

- Django: 3.2.4
- Django REST Framework: 3.15.1
- Python: 3.8.10

