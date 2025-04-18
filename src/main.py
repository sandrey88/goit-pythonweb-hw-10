from fastapi import FastAPI
from .routes import contacts, users
from src.database.db import engine
from src.database.models import Base

app = FastAPI(title="Contacts API")

# WARNING: Drop and recreate all tables for development reset
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# Create database tables
# Base.metadata.create_all(bind=engine)

app.include_router(contacts.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Contacts API!"}
