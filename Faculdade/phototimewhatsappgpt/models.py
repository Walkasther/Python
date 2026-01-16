# Definir os modelos de dados para as tabelas do banco de dados
class Sessao:
    def __init__(self, id, quiosque_id, codigo_sessao):
        self.id = id
        self.quiosque_id = quiosque_id
        self.codigo_sessao = codigo_sessao

class Foto:
    def __init__(self, id, caminho):
        self.id = id
        self.caminho = caminho
