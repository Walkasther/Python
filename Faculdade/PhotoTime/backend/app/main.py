# backend/app/main.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from database import models
from database.database import engine
from api.v1 import api

# Cria as tabelas no banco de dados (para desenvolvimento)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PhotoTime API",
    description="API para o sistema de quiosques de impressão de fotos PhotoTime.",
    version="1.0.0"
)

# Inclui todas as rotas da API sob o prefixo /api/v1
app.include_router(api.api_router, prefix="/api/v1")

# --- Servindo o Frontend do Quiosque ---

# Monta o diretório 'assets' para ser servido estaticamente
# O path deve ser relativo à raiz do projeto, então ajustamos
# para ../frontend-quiosque/assets quando rodamos de dentro de /app
# Em produção, essa configuração pode ser diferente.
app.mount("/assets", StaticFiles(directory="../frontend-quiosque/assets"), name="assets")

@app.get("/onboarding", response_class=FileResponse)
async def read_onboarding():
    """Serve a página de registro de um novo totem."""
    return FileResponse('../frontend-quiosque/onboarding.html')

@app.get("/", response_class=FileResponse)
async def read_index():
    """Serve a página principal do quiosque."""
    # Adicionaremos uma lógica para checar se o quiosque está registrado
    # Se não estiver, redirecionamos para /onboarding
    return FileResponse('../frontend-quiosque/index.html')

