from html import entities
from sqlalchemy.orm import Session
from entities.user import User
from models.database import db
from schemas import user

class UserModel():
    _entity = User

    def get_user_by_user_code( user_code: str):
        return db.query(User).filter(User.user_code == user_code).first()

