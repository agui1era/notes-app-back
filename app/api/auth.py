from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

router = APIRouter()

# Configuración JWT
SECRET_KEY = os.getenv("SECRET_KEY", "supersecreto2025")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# Seguridad de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Base de datos simulada
fake_users_db = {}

class User(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/register", response_model=Token)
async def register_user(user: User):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Usuario ya registrado")
    hashed_password = get_password_hash(user.password)
    fake_users_db[user.username] = {"username": user.username, "hashed_password": hashed_password}
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
async def login_user(user: User):
    db_user = fake_users_db.get(user.username)
    if not db_user or not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# 🔹 Ruta explícita para manejar OPTIONS en /login y evitar errores CORS
@router.options("/login")
async def options_login():
    headers = {
        "Access-Control-Allow-Origin": "*",  # Permitir cualquier origen
        "Access-Control-Allow-Methods": "OPTIONS, POST",  # Métodos permitidos
        "Access-Control-Allow-Headers": "*",  # Permitir cualquier encabezado
    }
    return JSONResponse(content={"message": "Método OPTIONS habilitado para /login"}, headers=headers)
