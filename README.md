# FastAPI Backend Server

A professional, production-ready FastAPI backend server with clean architecture, following best practices and industry standards.

## 🚀 Features

- **FastAPI Framework**: Modern, fast (high-performance) web framework
- **Clean Architecture**: Well-organized folder structure with separation of concerns
- **Authentication & Authorization**: JWT-based authentication with secure password hashing
- **Database Integration**: SQLAlchemy ORM with SQLite (easily switchable to PostgreSQL/MySQL)
- **API Versioning**: Structured API versioning (v1)
- **CORS Configuration**: Configurable CORS middleware
- **Pydantic Models**: Request/response validation with Pydantic
- **Environment Configuration**: Environment-based configuration management
- **Security**: Password hashing with bcrypt, JWT tokens
- **Auto-generated Documentation**: Interactive API docs (Swagger UI & ReDoc)
- **Logging**: Structured logging system
- **Testing Ready**: Test structure included

## 📁 Project Structure

```
Python-Server/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Application entry point
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── api.py          # API router aggregator
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           ├── auth.py     # Authentication endpoints
│   │           ├── users.py    # User management endpoints
│   │           └── items.py    # Item CRUD endpoints
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py           # Configuration settings
│   │   ├── security.py         # Security utilities (JWT, password hashing)
│   │   └── dependencies.py     # Dependency injection
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py             # Import all models here
│   │   ├── base_class.py       # Base SQLAlchemy model
│   │   ├── session.py          # Database session
│   │   └── init_db.py          # Database initialization
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py             # User database model
│   │   └── item.py             # Item database model
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py             # User Pydantic schemas
│   │   ├── item.py             # Item Pydantic schemas
│   │   └── token.py            # Token schemas
│   └── utils/
│       ├── __init__.py
│       └── logger.py           # Logging configuration
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Pytest configuration
│   └── api/
│       ├── __init__.py
│       └── v1/
│           ├── __init__.py
│           └── test_auth.py    # Authentication tests
├── alembic/                    # Database migrations
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
├── logs/                       # Application logs
├── .env.example                # Example environment variables
├── .gitignore                  # Git ignore file
├── requirements.txt            # Python dependencies
├── alembic.ini                 # Alembic configuration
└── README.md                   # This file
```

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Python-Server
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Initialize the database**
   ```bash
   alembic upgrade head
   ```

## 🚀 Running the Server

### Development Mode

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Production Mode

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

The server will start at `http://localhost:8000`

## 📚 API Documentation

Once the server is running, visit:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/api/v1/openapi.json

## 🔐 Authentication

The API uses JWT (JSON Web Tokens) for authentication.

### Register a new user

```bash
POST /api/v1/auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "johndoe",
  "password": "securepassword123",
  "full_name": "John Doe"
}
```

### Login

```bash
POST /api/v1/auth/login
Content-Type: application/x-www-form-urlencoded

username=user@example.com&password=securepassword123
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Using the token

Include the token in the Authorization header:
```bash
Authorization: Bearer <your-token>
```

## 🧪 Testing

Run tests with pytest:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=app tests/
```

## 📦 API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register a new user
- `POST /api/v1/auth/login` - Login and get access token

### Users
- `GET /api/v1/users/me` - Get current user
- `PUT /api/v1/users/me` - Update current user
- `GET /api/v1/users/` - Get all users (authenticated)
- `GET /api/v1/users/{user_id}` - Get user by ID

### Items
- `GET /api/v1/items/` - Get all items for current user
- `POST /api/v1/items/` - Create a new item
- `GET /api/v1/items/{item_id}` - Get item by ID
- `PUT /api/v1/items/{item_id}` - Update an item
- `DELETE /api/v1/items/{item_id}` - Delete an item

## 🔧 Configuration

Edit `.env` file to configure:

- `SECRET_KEY`: Secret key for JWT encoding
- `DATABASE_URL`: Database connection string
- `BACKEND_CORS_ORIGINS`: Allowed CORS origins
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time

## 🗄️ Database Migrations

Create a new migration:
```bash
alembic revision --autogenerate -m "Description of changes"
```

Apply migrations:
```bash
alembic upgrade head
```

Rollback migration:
```bash
alembic downgrade -1
```

## 🐳 Docker Support (Optional)

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:
```bash
docker build -t fastapi-server .
docker run -p 8000:8000 fastapi-server
```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 👤 Author

HB Tech - [hbtech-dev](https://github.com/hbtech-dev)

## ⭐ Show your support

Give a ⭐️ if this project helped you!
