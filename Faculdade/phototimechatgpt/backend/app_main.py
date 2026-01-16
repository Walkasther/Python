# backend/app_main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os

# Criar instância FastAPI
app = FastAPI(title="PhotoTime", description="Backend do quiosque PhotoTime", version="0.1")

# Caminho da pasta 'static'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Montar arquivos estáticos
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


# ---------- Rotas ----------

@app.get("/api/ping")
async def ping():
    """Rota de teste da API"""
    return {"message": "pong"}

@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve a página inicial do quiosque"""
    index_file = os.path.join(STATIC_DIR, "kiosk_index.html")
    return FileResponse(index_file)
