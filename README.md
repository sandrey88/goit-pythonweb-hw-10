# goit-pythonweb-hw-08

# FastAPI Contacts Management Application

REST API application for managing contacts with FastAPI framework.

## Technologies

- Python 3.9+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Poetry (dependency management)
- Docker & Docker Compose

## Features

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

### Contacts Management

- `GET /contacts` - Get list of all contacts
- `POST /contacts` - Create a new contact
- `GET /contacts/{contact_id}` - Get a specific contact by ID
- `PUT /contacts/{contact_id}` - Update an existing contact
- `DELETE /contacts/{contact_id}` - Delete a contact

### Search and Filtering

- `GET /contacts/find?q={query}` - Search contacts by name, surname, or email
- `GET /contacts/birthdays/next7days` - Get contacts with birthdays in the next 7 days

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
- 422: Validation error (invalid data format)
- 500: Internal server error
