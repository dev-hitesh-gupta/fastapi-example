from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User, UserDto
from repositories import UserRepository

router = APIRouter()


@router.post("/users/")
async def create_user(user: UserDto, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    return repo.create_user(user.get_db_model())


@router.get("/users/")
async def get_all_users(db: Session = Depends(get_db)):
    repo = UserRepository(db)
    return repo.get_all_users()


@router.get("/users/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    user = repo.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/users/{user_id}")
async def update_user(user_id: int, user: UserDto, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    existing_user = repo.update_user(user_id, user.get_db_model())
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    return existing_user


@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    user = repo.delete_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
