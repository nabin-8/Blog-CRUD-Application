# Blog CRUD Application

A comprehensive web application built with Django that allows users to perform Create, Read, Update, and Delete (CRUD) operations on blog posts. This project also includes user authentication using Django REST Framework and JSON Web Tokens (JWT). The application is containerized using Docker for easy setup and deployment.

## Features

- User authentication (login and registration)
- CRUD operations on blog posts
- Pagination for blog posts
- Docker implementation

## Technologies Used

- Django
- Django REST Framework
- SimpleJWT (for authentication)
- SQLite
- Docker

## Installation & Setup

### Prerequisites

Ensure you have the following installed:

- Docker
- Docker Compose
- Git

### Clone the Repository

```sh
https://github.com/nabin-8/Blog-CRUD-Application.git

cd backend
```

## Build and Run the Project with Docker

1.  Build the Docker images

    ```bash
    docker-compose build
    ```

2.  Run the project:
    ```bash
    docker-compose up
    ```

### Project Structure

<pre>
blog-crud-application/
├── backend/
│   ├── account/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── urls.py
│   ├── blog/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── blogs/
│   │   └── images/
│   ├── home/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── .dockerignore
│   ├── db.sqlite3
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── manage.py
│   └── requirements.txt
├── .gitignore
└── README.md
</pre>
