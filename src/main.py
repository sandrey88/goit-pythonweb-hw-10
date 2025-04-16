from fastapi import FastAPI
from .routes import contacts, users
from .database.db import engine
from .database.models import Base

app = FastAPI(title="Contacts API")

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(contacts.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Contacts API!"}
