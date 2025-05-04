from typing import Optional

from pydantic import BaseModel, Field, field_validator

class NoteModel(BaseModel):
    """
    NoteModel is a Pydantic model that represents the structure of a note.
    It includes fields for the note's title and content, along with validation rules.
    """
    title: Optional[str] = Field(default=None, title="Note Title", description="Title of the note")
    content: Optional[str] = Field(default=None, title="Note Content", description="Content of the note")

    @field_validator("content")
    def check_content(cls, value: str) -> str:
        if not value or len(value)<=10:
            raise ValueError("Content cannot be less than 10 characters")
        return value

    @field_validator("title")
    def check_title(cls, value: str) -> str:
        if not value or len(value)<=5:
            raise ValueError("Title cannot be less than 5 characters")
        return value


class UserRequest(BaseModel):
    """
    UserRequest is a Pydantic model that represents the structure of a user request.
    It includes fields for the user's ID, name, and email, along with validation rules.
    """
    username: Optional[str] = Field(default=None, title="User ID", description="ID of the user")
    password: Optional[str] = Field(default=None, title="User Password", description="Password of the user")
    
    @field_validator("username")
    def check_username_null(cls, value: str) -> str:
        if not value or len(value)<3:
            raise ValueError("Username cannot be less than 3 characters")
        return value

class TokenResponse(BaseModel):
    """
    TokenResponse is a Pydantic model that represents the structure of a token response.
    It includes fields for the access token, token type, and expiration time.
    """
    access_token: str = Field(default=None, title="Access Token", description="Access token for the user")
    token_type: str = Field(default=None, title="Token Type", description="Type of the token")
    expires_in: int = Field(default=None, title="Expiration Time", description="Expiration time in seconds")