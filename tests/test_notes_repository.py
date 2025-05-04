
from app.models.entity import Base, NoteEntity
from app.repository.note_repo import NoteRepository
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

import pytest

TEST_DB_URL = "sqlite:///:memory:"

@pytest.fixture(scope="function")
def get_test_db():
    engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False},poolclass=StaticPool)
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope="function")
def notes_repository(get_test_db):
    # Create a new instance of the NoteRepository for each test
    yield NoteRepository(get_test_db)


@pytest.mark.asyncio
async def test_save_note(notes_repository):
    # Test saving a note
    note_data = NoteEntity(
        id=1,
        title="Test Note",
        content="This is a test note.",
        user_id=1
    )
   
    await notes_repository.save_note(note_data)
    # Verify that the note was saved correctly
    saved_note = await notes_repository.find_note(1,1)
    assert saved_note is not None
    assert saved_note.title == "Test Note"
    assert saved_note.content == "This is a test note."

@pytest.mark.asyncio
async def test_find_note(notes_repository):
    # Test finding a note
    note_data = NoteEntity(
        id=2,
        title="Test Note 2",
        content="This is another test note.",
        user_id=1
    )
    
    await notes_repository.save_note(note_data)

    found_note = await notes_repository.find_note(2,1)
    assert found_note is not None
    assert found_note.title == "Test Note 2"
    assert found_note.content == "This is another test note."

@pytest.mark.asyncio
async def test_find_all_notes(notes_repository):
    # Test finding all notes for a user
    note_data1 = NoteEntity(
        id=3,
        title="Test Note 3",
        content="This is the third test note.",
        user_id=1
    )
    note_data2 = NoteEntity(
        id=4,
        title="Test Note 4",
        content="This is the fourth test note.",
        user_id=1
    )

    await notes_repository.save_note(note_data1)
    await notes_repository.save_note(note_data2)

    found_notes = await notes_repository.find_all_notes(1)
    assert len(found_notes) == 2
    assert found_notes[0].title == "Test Note 3"
    assert found_notes[1].title == "Test Note 4"
    