from typing import Annotated, Union

from fastapi import Depends, FastAPI, HTTPException, Query

from app.dependencies.object_config import get_authentication_service
from app.models.entity import UserEntity
from app.models.request_response import UserRequest
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 

from app.service.auth_service import AuthenticationService , get_current_user



from fastapi import APIRouter 

router = APIRouter(prefix="/auth")

@router.post("/")
async def create_user(form_data: UserRequest, auth: Annotated[AuthenticationService , Depends(get_authentication_service)]):
    # Check if the user already exists
    
    return await auth.register_user(form_data.username, form_data.password)

@router.post("/token")
async def generate_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth: Annotated[AuthenticationService , Depends(get_authentication_service)]
):
    # Validate user credentials and create JWT token
    return await auth.create_access_token(username=form_data.username, password=form_data.password)


@router.get("/me")
async def read_users_me(
    user: Annotated[dict,Depends(get_current_user)]
):
    # Get the current user based on the token
    return user