
from sqlalchemy import and_
from app.models.entity import NoteEntity

   
class NoteRepository:
    
    def __init__(self, db):
        self.db = db

    async def save_note(self, note: NoteEntity) -> NoteEntity:
        self.db.add(note)
        self.db.commit()
        self.db.refresh(note)
        return note
        
    async def find_note(self, note_id: int, user_id : int) -> NoteEntity:
        note = self.db.query(NoteEntity).filter(and_(NoteEntity.id == note_id,NoteEntity.user_id == user_id)).first()
        
        return note

    async def find_all_notes(self,user_id) -> list[NoteEntity]:
        notes = self.db.query(NoteEntity).filter(NoteEntity.user_id == user_id).all()
        if notes is None:
            raise Exception("No notes found")
        return notes



