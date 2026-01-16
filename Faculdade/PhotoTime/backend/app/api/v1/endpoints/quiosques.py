# backend/app/api/v1/endpoints/quiosques.py

import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database import database, models, schemas

router = APIRouter()


@router.post("/registrar", response_model=schemas.Quiosque)
def registrar_quiosque(
        quiosque_in: schemas.QuiosqueCreate,
        db: Session = Depends(database.get_db)
):
    """
    Registra um novo quiosque no sistema.

    - **nome_amigavel**: Um nome para identificar o quiosque (ex: "Shopping Morumbi").
    - Gera um `identificador_unico` que o quiosque deve salvar localmente.
    """
    identificador_unico = str(uuid.uuid4())

    db_quiosque = models.Quiosque(
        nome_amigavel=quiosque_in.nome_amigavel,
        identificador_unico=identificador_unico,
        status='ativo'  # Pode começar como ativo após o registro
    )

    db.add(db_quiosque)
    db.commit()
    db.refresh(db_quiosque)

    return db_quiosque


@router.post("/heartbeat")
def quiosque_heartbeat(
        # Aqui esperamos que o quiosque envie seu ID no header da requisição.
        # A implementação completa virá depois.
        # Ex: X-Quiosque-ID: <uuid>
):
    """
    Recebe um sinal de vida (heartbeat) de um quiosque para monitorar seu status.
    """
    # Lógica a ser implementada:
    # 1. Obter o identificador_unico do header.
    # 2. Buscar o quiosque no banco de dados.
    # 3. Atualizar o campo `ultimo_heartbeat` e `status` para 'ativo'.
    return {"status": "heartbeat recebido"}
