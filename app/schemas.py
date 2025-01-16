from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Esquema para crear una nueva nota
class NoteCreate(BaseModel):
    title: str
    content: str

# Esquema para representar una nota en las respuestas
class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    timestamp: datetime

    class Config:
        from_attributes = True  # Permite convertir SQLAlchemy Models a Pydantic

# Esquema para la creación de usuarios
class UserCreate(BaseModel):
    username: str
    password: str

# Esquema para representar un usuario en las respuestas
class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True  # Permite convertir SQLAlchemy Models a Pydantic
