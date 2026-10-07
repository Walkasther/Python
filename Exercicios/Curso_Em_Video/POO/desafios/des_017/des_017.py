# Crie a classe Produto, onde podemos cadastrar nome e preço.
# Crie também um método que mostre uma etiqueta de preço do produto.

from rich import print
from rich.traceback import install
install()


class Produto:
    '''
    cadastra e mostra nome e preço do produto
    '''
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    def etiqueta(self):
        from rich.panel import Panel
        conteudo = f'{self.nome:-^35} '\
                    f'\n{"-"*36}'\
                   f'\n{f'R${self.preco:,.2f}':.^36}'

        etiqueta = Panel(conteudo, title='Produto', width=40)
        return etiqueta


p1 = Produto('IPhone 17 Pro Max', 25_000.85)
print(p1.etiqueta())

p2 = Produto('Notebook Gamer', 8_000)
print(p2.etiqueta())