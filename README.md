# goit-pythonweb-hw-10

# FastAPI Contacts Management Application

REST API application for managing contacts with FastAPI framework.

## Technologies

- Python 3.9+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Poetry (dependency management)
- Docker & Docker Compose
- Cloudinary (avatar storage)

## Features

- User registration, login, email verification
- Rate limiting for sensitive endpoints (register, me)
- Avatar upload and storage via Cloudinary (with avatar_url field)
- CRUD operations for contacts
- Search contacts by name, surname, or email
- Get contacts with upcoming birthdays (next 7 days)
- Data validation using Pydantic
- Interactive API documentation (Swagger UI)
- Alternative API documentation (ReDoc)

## Prerequisites

- Python 3.9 or higher
- Poetry
- Docker and Docker Compose

## Installation

1. Clone the repository:

```bash
git clone https://github.com/sandrey88/goit-pythonweb-hw-10.git
cd goit-pythonweb-hw-10
```

2. Copy environment variables:

```bash
cp .env.example .env
```

Then edit `.env` with your settings.

3. Install dependencies with Poetry:

```bash
poetry install
```

## Environment Variables

The application uses a `.env` file for configuration. Example:

```env
DATABASE_URL=postgresql://user:password@db:5432/contacts_db
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=contacts_db
CLOUDINARY_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
MAIL_USERNAME=your_email@example.com
MAIL_PASSWORD=your_password
MAIL_FROM=your_email@example.com
MAIL_PORT=465
MAIL_SERVER=smtp.example.com
MAIL_STARTTLS=False
MAIL_SSL_TLS=True
SECRET_KEY=your_secret_key
```

## Running the Application

### Using Docker (recommended):

```bash
docker-compose up --build
```

The application will be available at http://localhost:8000

### Using Poetry (local development):

1. Start PostgreSQL (make sure it's running locally)

2. Create a `.env` file in the root directory with the following content:

```env
DATABASE_URL=postgresql://YOUR_USERNAME@localhost:5432/contacts_db
POSTGRES_USER=YOUR_USERNAME
POSTGRES_PASSWORD=YOUR_PASSWORD
POSTGRES_DB=contacts_db
```

Replace `YOUR_USERNAME` and `YOUR_PASSWORD` with your PostgreSQL credentials.

3. Create the database:

```bash
createdb contacts_db
```

4. Activate the virtual environment:

```bash
poetry shell
```

5. Install dependencies:

```bash
poetry install
```

6. Run the application:

```bash
poetry run uvicorn src.main:app --reload
```

## API Endpoints

### Authentication

- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and get JWT token
- `GET /auth/verify-email?token=...` - Verify email address
- `GET /auth/me` - Get current user info (JWT required)
- `PATCH /auth/avatar` - Upload or update user avatar (JWT required, file upload)

### Contacts Management

- `GET /contacts` - Get list of all contacts
- `POST /contacts` - Create a new contact
- `GET /contacts/{contact_id}` - Get a specific contact by ID
- `PUT /contacts/{contact_id}` - Update an existing contact
- `DELETE /contacts/{contact_id}` - Delete a contact

### Search and Filtering

- `GET /contacts/find?q={query}` - Search contacts by name, surname, or email
- `GET /contacts/birthdays/next7days` - Get contacts with birthdays in the next 7 days

## Rate Limiting

Sensitive endpoints (`/auth/register`, `/auth/me`) are protected by rate limiting (5 requests per minute per IP) to prevent abuse. If the limit is exceeded, a 429 error is returned.

## Avatar Upload (Cloudinary)

- Users can upload an avatar via the `/auth/avatar` endpoint using a file upload (image).
- Images are stored in Cloudinary, and the returned `avatar_url` field contains the public URL.
- Cloudinary credentials must be set in the `.env` file.

## Data Validation

The API implements strict data validation:

- `first_name` and `last_name`: 2-50 characters
- `email`: Must be a valid email address
- `phone`: 10-20 characters
- `birthday`: Valid date in YYYY-MM-DD format
- `additional_data`: Optional field

Example of valid contact data:

```json
{
  "first_name": "Іван",
  "last_name": "Петренко",
  "email": "ivan@example.com",
  "phone": "0501234567",
  "birthday": "1990-01-15",
  "additional_data": "Додаткова інформація"
}
```

## API Documentation

Once the application is running, you can access:

- Swagger UI documentation at http://localhost:8000/docs
- ReDoc documentation at http://localhost:8000/redoc

## Error Handling

- 404: Contact not found
- 409: User already exists or duplicate email
- 401: Invalid credentials
- 403: Email not verified
- 429: Too many requests (rate limit exceeded)
- 422: Validation error (invalid data format)
- 500: Internal server error
