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
   python3 -m venv venv

3. **Activate the virtual environment:**
    
   ```bash
   source venv/bin/activate

4. **Install the required packages:**
    
   ```bash
   pip install -r requirements.txt

5. **Set up the database:** 
      ```bash
      Create Database in postgresql 
   
      psql -U postgres
       - CREATE USER newuser WITH PASSWORD 'password';
       - CREATE DATABASE newdatabase;
       - GRANT ALL PRIVILEGES ON DATABASE newdatabase TO newuser;
       \q # to exit from postgresql

      replace .env.example with .env
      Update below database settings in .env with your PostgreSQL credentials.
       - DB_NAME
       - DB_USER
       - DB_PASSWORD
      

6. **Database migrate:**
    
   ```bash
   python3 manage.py migrate

7. **Create a superuser:**
    
   ```bash
   python3 manage.py createsuperuser

8. **Run Redis server (if using Redis for caching):**
    
   ```bash
   redis-server

9. **Running the Application:**
    
   ```bash
   python3 manage.py runserver

   You can now access the application at http://127.0.0.1:8000/.


10. **API Documentation:**
    
   ```bash
   http://127.0.0.1:8000/swagger/


11. **Running Tests:**
    
   ```bash
   pytest

