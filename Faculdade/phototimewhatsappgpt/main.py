from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.requests import Request
import mysql.connector
import uuid
import os

app = FastAPI()

# Configuração do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'database': 'seu_banco_de_dados'
}

# Função para conectar ao banco de dados
def get_db():
    db = mysql.connector.connect(**db_config)
    return db

# Endpoint para upload de fotos
@app.post("/api/upload")
async def upload_foto(foto: UploadFile = File(...)):
    # Salvar a foto no servidor
    foto_nome = f"{uuid.uuid4().hex}.jpg"
    foto_caminho = f"fotos/{foto_nome}"
    with open(foto_caminho, "wb") as f:
        f.write(foto.file.read())

    # Salvar o caminho da foto no banco de dados
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO fotos (caminho) VALUES (%s)"
    cursor.execute(query, (foto_caminho,))
    db.commit()

    return JSONResponse(content={"mensagem": "Foto salva com sucesso!"}, status_code=201)
