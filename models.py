from sqlalchemy import Column, Integer, String, TypeDecorator, PickleType
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)


class UserDto(BaseModel):
    name: str | None = None
    email: str
    password: str | None = None

    def get_db_model(self):
        user = User()
        user.name = self.name
        user.email = self.email
        user.password = self.password
        return user
