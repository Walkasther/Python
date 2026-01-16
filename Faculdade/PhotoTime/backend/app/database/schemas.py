# backend/app/database/schemas.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# --- Quiosque Schemas ---

class QuiosqueBase(BaseModel):
    nome_amigavel: str
    localizacao: Optional[str] = None

class QuiosqueCreate(BaseModel):
    nome_amigavel: str

class Quiosque(QuiosqueBase):
    id: int
    identificador_unico: str
    status: str
    ultimo_heartbeat: Optional[datetime]
    data_criacao: datetime

    class Config:
        orm_mode = True

# --- Admin Schemas ---

class AdminCreate(BaseModel):
    nome: str
    email: str
    senha: str

class AdminLogin(BaseModel):
    email: str
    senha: str

class Token(BaseModel):
    access_token: str
    token_type: str
