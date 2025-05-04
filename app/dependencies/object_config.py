from sqlalchemy.orm import Session
from fastapi import Depends
from app.repository.engine import get_db
from app.repository.note_repo import NoteRepository
from app.repository.user_repo import UserRepository
from app.service.auth_service import AuthenticationService
from app.service.ml_service import SentimentAnalysisService


def get_user_repo(db: Session = Depends(get_db)):
    return UserRepository(db)

def get_note_repo(db: Session = Depends(get_db)):
    return NoteRepository(db)

def get_authentication_service(user_repo: UserRepository = Depends(get_user_repo)):
    return AuthenticationService(user_repo)

def get_sentiment_analysis_service():
    return SentimentAnalysisService()

