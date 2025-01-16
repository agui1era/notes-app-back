from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Importa el módulo completo en lugar de solo funciones específicas
import app.api.auth as auth

# Crear instancia de FastAPI
app = FastAPI()

# Modelos para solicitudes
class User(BaseModel):
    username: str
    password: str

# Ruta principal
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

# Ruta para registrar usuario
@app.post("/api/auth/register")
async def register_user(user: User):
    try:
        return auth.register_user_logic(user)  # Llama directamente al módulo
    except HTTPException as e:
        raise e

# Ruta para iniciar sesión
@app.post("/api/auth/login")
async def login_user(user: User):
    try:
        return auth.login_user_logic(user)  # Llama directamente al módulo
    except HTTPException as e:
        raise e
