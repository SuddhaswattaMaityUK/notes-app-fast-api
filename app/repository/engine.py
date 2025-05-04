

from sqlalchemy import create_engine
from app.models.entity import Base
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DATABASE_URL = 'sqlite:///./notes.db'


def custom_engine():
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
    Base.metadata.create_all(bind=engine)
    return engine

def get_db():
    engine = custom_engine()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
