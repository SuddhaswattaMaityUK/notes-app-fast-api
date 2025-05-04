from app.models.entity import UserEntity
from app.repository.engine import get_db
from fastapi import Depends

class UserRepository:
    def __init__(self, db):
        self.db = db

    async def save_user(self, user : UserEntity):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    
    async def find_user_by_username(self, username : str):
        return self.db.query(UserEntity).filter_by(username=username).first()
