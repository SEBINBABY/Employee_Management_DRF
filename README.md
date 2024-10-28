# Employee_Management_DRF
A project in Django Rest Framework which performs CRUD Operations for Employee Management.

## Table of Contents

* Features

* Technical Requirements

* Installation

* Usage

* API Documentation

## Features

### 1. Employee Profile Management:

* Create, retrieve, update, and delete employee profiles.
* Token Authentication to secure Endpoints, Filtering and Pagination.

## Technical Requirements

* Django (latest stable version)

* Django REST Framework (latest stable version)

* Token-based authentication

* PEP 8 compliant code

* Comprehensive data validations

* Django ORM for database interactions

## Installation

#### 1.Create and activate a virtual environment:

python -m venv .newvenv
source .newvenv/bin/activate

#### 2. Install dependencies:

pip install django==5.1.2

pip install -U djangorestframework (Version : 3.15.2 is used here)

pip install django-filter

#### 3. Run migrations:

python manage.py makemigrations

python manage.py migrate

#### 4. Run:

python manage.py runserver

## API

```bash

http://127.0.0.1:8000/admin/

http://127.0.0.1:8000/api/employees/

http://127.0.0.1:8000/api/employees/<int:id>/

## API Documentation

Please refer to this documentation for detailed information about each API endpoint, including input parameters, authentication requirements, and response formats.

Sample JSON for Creating a New Employee
{
"name": "Kiran",

"email": "kiran@gmail.com",

"department": "HR",

"role": "Manager"
}

## Employee Endpoints

### 1.Create a new Employee:

URL: POST /api/employees/ Payload Example:

    json

    {

        "name": "employee_name",

        "email": "employee@gmail.com",

        "department": "Engineering",

        "role": "Developer"

    }

*Authentication: Token-based authentication required.

### 2. List all Employees:

URL: GET /api/employees/

Authentication: Token-based authentication required.

Retrieve a specific employee's details:

URL: GET /api/employees/{id}/

Authentication: Token-based authentication required.

Update a employee's details:

URL: PUT /api/employees/{id}/

Payload Example:

json
 
{
"id": 1,

"name": "Updated_Employee_Name",

"email": "Updated_Email",

"department": "Updated_department",

"role": "Updated_role"

}

*Authentication: Token-based authentication required.

### 3. Delete a vendor:

URL: DELETE /api/employees/{id}/

Authentication: Token-based authentication required.

### 4. Filtering - Allow filtering of employees by department and role:

URL:  GET /api/employees/?department=HR&role=Manager

*Authentication: Token-based authentication required.

### 5. Pagination -  Limit results per page to 10 employees with pagination support :

URL:  GET/api/employees/?page=2

*Authentication: Token-based authentication required.


*Authentication: Token-based authentication required. Please note that you should replace {id} in the URLs with the actual employee ID you want to interact with.

Ensure you have the appropriate authentication token and include it in the request headers for endpoints that require authentication. Also, adjust the payload examples based on the actual structure and requirements of your Django application.

