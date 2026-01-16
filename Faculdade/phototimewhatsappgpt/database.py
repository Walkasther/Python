import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'database': 'seu_banco_de_dados'
}

def get_db():
    db = mysql.connector.connect(**db_config)
    return db

