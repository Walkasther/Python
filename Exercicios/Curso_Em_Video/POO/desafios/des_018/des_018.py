# Crie uma classe Churrasco, onde seja possível informar quantas pessoas vão participar e mostre quanto de carne deve
# ser comprado, o custo total do churrasco e o preço por pessoa.

from rich import print

class Churrasco:

    def __init__(self, titulo, quantidade, kilo=82.40, consumo=0.4):
        self.titulo = titulo
        self.quantidade = quantidade
        self.preco_do_kilo = kilo
        self.consumo_por_pessoa = consumo
        self.custo_por_pessoa = self.consumo_por_pessoa * self.preco_do_kilo
        self.quantidade_de_carne_total = self.consumo_por_pessoa * quantidade
        self.custo_total = self.custo_por_pessoa * quantidade


    def analisar(self):
        from rich.panel import Panel
        impresso = Panel(f'Analisando [green]{self.titulo}[/] com [blue]{self.quantidade} convidados[/]'
                         f'\nCada participante comerá {self.consumo_por_pessoa:.3f}Kg e cada kg custará R${self.preco_do_kilo:,.2f}'
                         f'\nRecomendo [blue]comprar {self.quantidade_de_carne_total:.3f}Kg[/] de carne'
                         f'\nO custo total será de [green]R${self.custo_total:,.2f}[/]'
                         f'\nCada pessoa pagará [yellow]R${self.custo_por_pessoa:,.2f}[/] para participar.', title=self.titulo,width=200)
        return impresso


c1 = Churrasco('Churras dos Amigos', 15)
print(c1.analisar())
