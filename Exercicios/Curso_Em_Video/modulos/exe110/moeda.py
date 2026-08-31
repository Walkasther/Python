from modulos.exe109 import moeda
from modulos.uteis import cabecalho

def resumo(numero, aumento, reducao, formatado=True):
    cabecalho('RESUMO DO VALOR')
    print(f'{"Preço analisado:":<20}{moeda.moeda(numero)}')
    print(f'{"Dobro do preço:":<20}{moeda.dobro(numero, formatado)}')
    print(f'{"Metade do preço:":<20}{moeda.metade(numero, formatado)}')
    print(f'{f"{aumento}% de aumento:":<20}{moeda.aumentar(numero, aumento, formatado)}')
    print(f'{f"{reducao}% de redução:":<20}{moeda.diminuir(numero, reducao, formatado)}')
    cabecalho()