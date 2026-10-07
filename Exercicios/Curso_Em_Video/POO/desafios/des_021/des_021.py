# Crie a classe Caneta, que simule o funcionamento de uma caneta colorida. Podendo escrever frases na cor relativa.

from rich import print

class Caneta:
    def __init__(self,cor):
        self.cor = 'red' if cor == "vermelha" else "blue" if cor == 'azul' else 'green' if cor == 'verde' else cor
        self.tampada = True


    def destampar(self):
        self.tampada = False


    def tampar(self):
        self.tampada = True


    def escrever(self,texto):
        if self.tampada:
            print(f"\n🚫 A [{self.cor}]Caneta {self.cor}[/] está tampada!", end='')
        else:
            print(f'[{self.cor}]{texto}[/]', end=' ')


    def quebrar_linha(self, qtd):
        print('\n' * qtd)


c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")
c4 = Caneta('yellow')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem?")
c1.quebrar_linha(2)
c2.escrever("Olá Gafanhoto!")
c3.escrever("Vamos exercitar!")
c4.escrever('')

c1.tampar()
c2.tampar()
c3.tampar()
c4.tampar()