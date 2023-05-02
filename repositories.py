from sqlalchemy.orm import Session

from models import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_all_users(self):
        return self.db.query(User).all()

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def update_user(self, user_id: int, user: User):
        existing_user = self.db.query(User).filter(User.id == user_id).first()
        existing_user.name = user.name
        existing_user.email = user.email
        existing_user.password = user.password
        self.db.commit()
        return existing_user

    def delete_user(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        self.db.delete(user)
        self.db.commit()
        return user
