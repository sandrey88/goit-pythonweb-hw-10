# goit-pythonweb-hw-08

# Contacts API

A FastAPI-based REST API for managing contacts with PostgreSQL database.

## Features

- CRUD operations for contacts
- Search contacts by name, surname, or email
- Get contacts with upcoming birthdays (next 7 days)
- Data validation using Pydantic
- Interactive API documentation (Swagger UI)
- Alternative API documentation (ReDoc)

## Prerequisites

- Python 3.12.1
- PostgreSQL 14+

## Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure PostgreSQL:

   - Install PostgreSQL if not installed: `brew install postgresql@14`
   - Start PostgreSQL service: `brew services start postgresql@14`
   - Create a database: `createdb contacts_db`

4. Run the application:

```bash
uvicorn src.main:app --reload
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

After running the application, visit:

- Swagger UI: `http://localhost:8000/docs` - Interactive documentation with the ability to test endpoints
- ReDoc: `http://localhost:8000/redoc` - Alternative documentation with better readability

## Error Handling

- 404: Contact not found
- 422: Validation error (invalid data format)
- 500: Internal server error
