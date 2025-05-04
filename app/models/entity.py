from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Base(DeclarativeBase):
    pass

class NoteEntity(Base):
    __tablename__ = 'notes'
    id: Mapped[int] = mapped_column(primary_key=True, index=True ,unique=True)
    title: Mapped[str] = mapped_column(index= False)
    content: Mapped[str] = mapped_column(index=False)
    user_id: Mapped[int] = mapped_column(index=False)

class UserEntity(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, index=True ,unique=True)
    username: Mapped[str] = mapped_column(index=True)
    password: Mapped[str] = mapped_column(index=False)