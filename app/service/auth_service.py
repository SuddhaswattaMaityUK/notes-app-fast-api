SECRET_KEY = 'awcaxqweqxasaxadas'
ALGORITHM = 'HS256'

from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Annotated
from jose import jwt
from app.repository.user_repo import UserRepository
from app.models.request_response import UserRequest
from fastapi import Depends, HTTPException
from app.models.entity import UserEntity
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


class AuthenticationService :
    
    def __init__(self, repo : UserRepository ):
        self.repo = repo
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    async def register_user(self, username, password):
        user_entity = UserEntity(
                                    username=username,
                                    password=self.pwd_context.hash(password),
                                )
        # Check if the user already exists
        existing_user = await self.repo.find_user_by_username(username)
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already registered")
        # Create the user
        await self.repo.save_user(user_entity)
        return {"message": "User created successfully"}


    async def create_access_token(self, username: str , password: str):
        user_entity = await self.repo.find_user_by_username(username)
        if not user_entity:
            raise HTTPException(status_code=400, detail="Invalid username or password")
        if not self.pwd_context.verify(password, user_entity.password):
            raise HTTPException(status_code=400, detail="Invalid username or password")
        
        # Create JWT token
        access_token_expires = timedelta(minutes=30)
        access_token = jwt.encode(
            {"sub": user_entity.username,"id":user_entity.id, "exp": datetime.utcnow() + access_token_expires},
            SECRET_KEY,
            algorithm=ALGORITHM,
        )
        return {"access_token": access_token, "token_type": "bearer"}
    

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise credentials_exception
    except jwt.JWTError:
        raise credentials_exception
    
    return {'id':user_id, 'username':username}

    
        
    