from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.schemas import UserCreate, UserRead, UserLogin
from src.repository import users as user_repo
from src.database.db import get_db
from src.auth_jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_repo.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=409, detail="User with this email already exists")
    created_user = user_repo.create_user(db, user)
    if not created_user:
        raise HTTPException(status_code=409, detail="User creation failed (possibly duplicate email)")
    return created_user

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = user_repo.authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    # Генеруємо JWT-токен
    token = create_access_token({"sub": db_user.email, "user_id": db_user.id})
    return {"access_token": token, "token_type": "bearer"}
