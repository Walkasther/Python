# backend/app/api/v1/api.py

from fastapi import APIRouter
from endpoints import quiosques

api_router = APIRouter()

# Inclui todos os endpoints relacionados a quiosques
api_router.include_router(quiosques.router, prefix="/quiosques", tags=["Quiosques"])

# Futuramente, adicionaremos outros roteadores aqui:
# from .endpoints import sessoes, admin
# api_router.include_router(sessoes.router, prefix="/sessoes", tags=["Sessões"])
# api_router.include_router(admin.router, prefix="/admin", tags=["Admin"])
