# Crie uma classe Funcionario, onde podemos cadastrar nome, setor e cargo.
# Crie também um método que permita ao funcionário se apresentar.

from rich import print
from rich import inspect

class Funcionario:
    """
    Cadastra um funcionário novo, seu setor e sua profissão, além de fazer uma apresentação
    """
    empresa = 'Curso em Vídeo'


    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    def apresentacao(self):
        return f':handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} no setor de {self.setor} da empresa {Funcionario.empresa}'



c1 = Funcionario('Maria', 'Administração','Diretora')
c1.empresa = 'Estudonauta'
print(c1.apresentacao())

c2 = Funcionario('Pedro', 'TI','Programador')
print(c2.apresentacao())

inspect(c1)
inspect(c2)