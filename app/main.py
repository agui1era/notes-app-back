from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.notes import router as notes_router

app = FastAPI(title="Notes API", description="API para gestión de notas")

# Rutas principales
app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])
app.include_router(notes_router, prefix="/api/notes", tags=["Notes"])

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de notas"}
