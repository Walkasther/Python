# Funções úteis para o projeto
def gerar_codigo_sessao():
    return str(uuid.uuid4().int)[:8]
