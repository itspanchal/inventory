# Inventory Management System

This project is an Inventory Management System built using Django and Django REST Framework (DRF). It provides a RESTful API for managing inventory items, including creating, reading, updating, and deleting items.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [API Documentation](#api-documentation)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or later
- pip (Python package installer)
- PostgreSQL (or any other database of your choice)
- Redis (for caching)
- Virtual environment (recommended)

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/inventory-management-system.git
   cd inventory-management-system

2. **Create a virtual environment:**

   ```bash
   python -m venv venv

3. **Activate the virtual environment:**
    
   ```bash
   source venv/bin/activate

4. **Install the required packages:**
    
   ```bash
   pip install -r requirements.txt

5. **Set up the database:**
    Update your database settings in settings.py with your PostgreSQL credentials.
    
   ```bash
   python manage.py migrate

6. **Create a superuser:**
    
   ```bash
   python manage.py createsuperuser

7. **Run Redis server (if using Redis for caching):**
    
   ```bash
   redis-server

8. **Running the Application:**
    
   ```bash
   python manage.py runserver

   You can now access the application at http://127.0.0.1:8000/.

9. **Running Tests:**
    
   ```bash
   pytest

9. **API Documentation:**
    
   ```bash
   http://127.0.0.1:8000/swagger/
