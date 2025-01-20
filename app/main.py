from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.auth import router as auth_router
from app.api.notes import router as notes_router

# Crear la instancia de FastAPI
app = FastAPI(title="Notes API", description="API para gestión de notas")

# Configuración de CORS para permitir cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir cualquier origen (⚠ Úsalo con precaución en producción)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir cualquier encabezado
)

# Incluir los routers de autenticación y notas
app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])
app.include_router(notes_router, prefix="/api/notes", tags=["Notes"])

# Ruta de prueba para verificar que el servidor está funcionando
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de notas"}
