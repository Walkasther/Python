# backend/app/database/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ATENÇÃO: Substitua com as suas credenciais reais do MySQL.
# É altamente recomendável usar variáveis de ambiente para isso.
DATABASE_URL = "mysql+pymysql://user:password@localhost/phototime_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para obter uma sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
