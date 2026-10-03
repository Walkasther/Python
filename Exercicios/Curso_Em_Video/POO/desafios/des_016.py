# Crie uma classe Funcionario, onde podemos cadastrar nome, setor e cargo.
# Crie também um método que permita ao funcionário se apresentar.

from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    def apresentacao(self):
        return f':handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} no setor de {self.setor} da empresa Curso em vídeo'



c1 = Funcionario('Maria', 'Administração','Diretora')
print(c1.apresentacao())

c2 = Funcionario('Pedro', 'TI','Programador')
print(c2.apresentacao())