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
git clone https://github.com/nabin-8/Blog-CRUD-Application.git
cd Blog-CRUD-Application/backend/
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

## API Endpoints

User Registration

Endpoint: POST http://0.0.0.0:8000/api/account/register/

Request Body:

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "username": "john08",
  "password": "john123"
}
```

Response (Success - 201):

```json
{
  "data": {},
  "message": "Account Created"
}
```

User Login

Endpoint: POST http://0.0.0.0:8000/api/account/login/

Request Body:

```json
{
  "username": "john08",
  "password": "john123"
}
```

Response (Success):

```json
{
  "message": "Login Success",
  "data": {
    "token": {
      "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0MDgwNjMzMCwiaWF0IjoxNzQwNzE5OTMwLCJqdGkiOiI1NmUwNDhiMTY0YmM0NjQxYWM2YWMyOTMyNDY0NTM5NyIsInVzZXJfaWQiOjF9.HqG9yn8EQmdHHdmB14TGwS76gpMUlNxsErxq2A4xAqM",
      "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQwNzIwMjMwLCJpYXQiOjE3NDA3MTk5MzAsImp0aSI6ImEzZGY1NWYxZTdhZjRhOGViN2JjMzg3MTE4Mjc2Y2M5IiwidXNlcl9pZCI6MX0.C6hqXEPWi648QD3Schi213Nfl1zP4G7a5TLAXVdR0n8"
    }
  }
}
```

### Blog CRUD Operations

**Create Blog Post**

Endpoint: POST http://0.0.0.0:8000/api/home/blog/

Authorization Required: Yes (Bearer token)

Request Headers:

```
Authorization: Bearer <access_token>
```

Request Body:

```json
{
  "title": "This is first title",
  "content": "content of blog app",
  "main_image": "<file>"
}
```

Response (If Not Authorized):

```json
{
  "detail": "Authentication credentials were not provided."
}
```

Response (Validation Error):

```json
{
  "data": {
    "title": ["This field is required."],
    "content": ["This field is required."],
    "main_image": ["No file was submitted."]
  },
  "message": "something went wrong"
}
```

Response (Success):

```json
{
  "data": {
    "id": "0eaed795-6643-4d54-9d78-77cd7ff50a16",
    "title": "This is first title",
    "content": "content of blog app",
    "main_image": "/blogs/Screenshot_from_2024-10-20_15-46-54.png",
    "user": 1
  },
  "message": "Blog Created Successfully"
}
```

**Get Blog Posts**

Endpoint: GET http://0.0.0.0:8000/api/home/blog/

Response:

```json
{
  "data": [
    {
      "id": "0eaed795-6643-4d54-9d78-77cd7ff50a16",
      "title": "This is first title",
      "content": "content of blog app",
      "main_image": "/blogs/Screenshot_from_2024-10-20_15-46-54.png",
      "user": 1
    }
  ],
  "message": "Blog Fetched Successfully"
}
```

**Update Blog Post**

Endpoint: PATCH http://0.0.0.0:8000/api/home/blog/

Request Body:

```json
{
  "id": "0eaed795-6643-4d54-9d78-77cd7ff50a16",
  "title": "updated blog",
  "content": "content of blog app",
  "main_image": "/blogs/Screenshot_from_2024-10-20_15-46-54.png",
  "user": 1
}
```

Response (Success):

```json
{
  "data": {
    "id": "0eaed795-6643-4d54-9d78-77cd7ff50a16",
    "title": "updated blog",
    "content": "content of blog app",
    "main_image": "/blogs/Screenshot_from_2024-10-20_15-46-54.png",
    "user": 1
  },
  "message": "Blog Updated Successfully"
}
```

**Delete Blog Post**

Endpoint: DELETE http://0.0.0.0:8000/api/home/blog/

Request Body:

```json
{
  "id": "0eaed795-6643-4d54-9d78-77cd7ff50a16"
}
```

Response (Success):

```json
{
  "data": {},
  "message": "Blog Deleted Successfully"
}
```

**Paginated Blog Posts**

Endpoint: GET http://0.0.0.0:8000/api/home/posts/

Response:

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "cef8482f-0857-4479-add1-bf146bf63d6e",
      "title": "This is first title",
      "content": "content of blog app",
      "main_image": "http://0.0.0.0:8000/blogs/Screenshot_from_2024-10-20_15-46-54_zXOqPcL.png",
      "user": 1
    }
  ]
}
```
