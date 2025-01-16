from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.core.database import get_db
from app.core.models import Note
from app.schemas import NoteCreate, NoteResponse

router = APIRouter()

@router.post("/", response_model=NoteResponse)
async def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    new_note = Note(
        title=note.title,
        content=note.content
    )  # `timestamp` y `updated_at` se manejan automáticamente por SQLAlchemy
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

@router.get("/", response_model=list[NoteResponse])
async def get_notes(db: Session = Depends(get_db)):
    return db.query(Note).all()

@router.put("/{note_id}", response_model=NoteResponse)
async def update_note(note_id: int, note: NoteCreate, db: Session = Depends(get_db)):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    
    db_note.title = note.title
    db_note.content = note.content
    db.commit()  # `updated_at` se actualiza automáticamente
    db.refresh(db_note)
    return db_note

@router.delete("/{note_id}")
async def delete_note(note_id: int, db: Session = Depends(get_db)):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    
    db.delete(db_note)
    db.commit()
    return {"message": "Nota eliminada"}
