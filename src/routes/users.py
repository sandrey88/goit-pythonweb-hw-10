from fastapi import APIRouter, Depends, HTTPException, status, Form, BackgroundTasks
from sqlalchemy.orm import Session
from src.schemas import UserCreate, UserRead, UserLogin
from src.repository import users as user_repo
from src.database.db import get_db
from src.auth_jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db), background_tasks: BackgroundTasks = None):
    db_user = user_repo.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=409, detail="User with this email already exists")
    created_user = user_repo.create_user(db, user, background_tasks)
    if not created_user:
        raise HTTPException(status_code=409, detail="User creation failed (possibly duplicate email)")
    return created_user

@router.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    db_user = user_repo.authenticate_user(db, username, password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not db_user.is_verified:
        raise HTTPException(status_code=403, detail="Email not verified. Please check your email to verify your account.")
    token = create_access_token({"sub": db_user.email, "user_id": db_user.id})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/verify-email")
def verify_email(token: str, db: Session = Depends(get_db)):
    user = db.query(user_repo.User).filter(user_repo.User.verification_token == token).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid or expired verification token")
    user.is_verified = True
    user.verification_token = None
    db.commit()
    return {"message": "Email successfully verified! You can now log in."}
