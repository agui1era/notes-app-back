# 📝 Notes App Backend (FastAPI + PostgreSQL)

Este es el backend del proyecto **Notes App**, construido con **FastAPI** y utilizando **PostgreSQL** como base de datos. 

---

## 📌 **Requisitos**
- **Python 3.8+**
- **PostgreSQL**
- **Git**
- **Docker (opcional)**

---

## 🚀 **Configuración y Ejecución**

### 📌 **1. Clonar el repositorio**
```sh
git clone https://github.com/tu-usuario/notes-app-backend.git
cd notes-app-backend
```

### 📌 **2. Crear y activar el entorno virtual**
```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 📌 **3. Instalar dependencias**
```sh
pip install -r requirements.txt
```

### 📌 **4. Configurar variables de entorno**
Crea un archivo **`.env`** en la raíz y agrega:
```
DATABASE_URL=postgresql://appuser:P0stgr3s#2025!@localhost:5432/notesdb
SECRET_KEY=supersecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 📌 **5. Configurar la base de datos con Alembic**
```sh
alembic upgrade head
```

### 📌 **6. Iniciar el servidor FastAPI**
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
> 🔹 La API estará disponible en **http://127.0.0.1:8000**

---

## 🛠 **Estructura del Proyecto**
```
notes-app-backend/
│── app/
│   ├── api/
│   │   ├── auth.py
│   │   ├── notes.py
│   ├── core/
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── config.py
│   ├── schemas/
│   ├── main.py
│── tests/
│── alembic/
│── alembic.ini
│── .env
│── requirements.txt
│── README.md
```

---

## 📌 **Endpoints Disponibles**
Puedes probar los endpoints en **http://127.0.0.1:8000/docs** o usando **cURL**:

### 📌 **Registro de usuario**
```sh
curl -X POST "http://127.0.0.1:8000/api/auth/register" \
-H "Content-Type: application/json" \
-d '{"username": "adminuser", "password": "S3cur3P@ss2025"}'
```

### 📌 **Inicio de sesión**
```sh
curl -X POST "http://127.0.0.1:8000/api/auth/login" \
-H "Content-Type: application/json" \
-d '{"username": "adminuser", "password": "S3cur3P@ss2025"}'
```
> 🔹 **Guarda el token de acceso** para usar en los siguientes endpoints.

### 📌 **Crear una nota**
```sh
curl -X POST "http://127.0.0.1:8000/api/notes/" \
-H "Authorization: Bearer TOKEN" \
-H "Content-Type: application/json" \
-d '{"title": "Nueva Nota", "content": "Contenido de la nota"}'
```

### 📌 **Obtener todas las notas**
```sh
curl -X GET "http://127.0.0.1:8000/api/notes/" \
-H "Authorization: Bearer TOKEN"
```

### 📌 **Actualizar una nota**
```sh
curl -X PUT "http://127.0.0.1:8000/api/notes/1" \
-H "Authorization: Bearer TOKEN" \
-H "Content-Type: application/json" \
-d '{"title": "Nota Actualizada", "content": "Nuevo contenido"}'
```

### 📌 **Eliminar una nota**
```sh
curl -X DELETE "http://127.0.0.1:8000/api/notes/1" \
-H "Authorization: Bearer TOKEN"
```

---

## 📌 **Ejecución con Docker (Opcional)**
Si prefieres usar Docker, ejecuta:
```sh
docker-compose up --build
```

Esto levantará el backend con PostgreSQL sin necesidad de configurarlo manualmente.

