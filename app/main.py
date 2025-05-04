from typing import Annotated, Union

from fastapi import Depends, FastAPI, HTTPException, Query

from app.models.entity import NoteEntity, UserEntity
from app.models.request_response import NoteModel, UserRequest
from app.service.ml_service import SentimentAnalysisService
from app.service.auth_service import AuthenticationService
from app.repository.note_repo import NoteRepository
from app.repository.user_repo import UserRepository

from app.routers.notes_router import router as  notes_router
from app.routers.auth_router import router as auth_router

app = FastAPI()
app.include_router(notes_router)
app.include_router(auth_router)




