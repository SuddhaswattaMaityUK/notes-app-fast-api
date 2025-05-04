
from fastapi import  APIRouter
from typing import Annotated, Union

from fastapi import Depends, FastAPI, HTTPException, Query

from app.dependencies.object_config import get_note_repo, get_sentiment_analysis_service
from app.models.entity import NoteEntity
from app.models.request_response import NoteModel, UserRequest
from app.service.ml_service import SentimentAnalysisService
from app.service.auth_service import get_current_user
from app.repository.note_repo import NoteRepository
from app.repository.user_repo import UserRepository


router = APIRouter(prefix="/notes")

@router.post("/")
async def create_note(user: Annotated[dict,Depends(get_current_user)],note: NoteModel, repo: Annotated[ NoteRepository , Depends(get_note_repo)]): 
    # Check if the note already exists
    print(user)
    note_entity = NoteEntity(
        title=note.title,
        content=note.content,
        user_id=user['id']
    )
    return await repo.save_note(note_entity)
   

@router.get("/{note_id}")
async def read_note(user: Annotated[dict,Depends(get_current_user)],note_id: int,repo: Annotated[NoteRepository ,Depends(get_note_repo)]) :
    # Check if the note exists
    note = await repo.find_note(note_id,user['id'])
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.get("/")
async def read_notes(user: Annotated[dict,Depends(get_current_user)],repo : Annotated[NoteRepository , Depends(get_note_repo)]):
    all_notes = await repo.find_all_notes(user['id'])
    return all_notes

@router.get("/analyse/{note_id}" )
async def analyse_note(user: Annotated[dict,Depends(get_current_user)],note_id: int,  repo: Annotated[NoteRepository , Depends(get_note_repo)],ml_service: Annotated[SentimentAnalysisService,Depends(get_sentiment_analysis_service)]):
    # Check if the note exists
    note = await repo.find_note(note_id, user['id'])
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    sentiment = await ml_service.analyze_sentiment(note.content)
    return sentiment