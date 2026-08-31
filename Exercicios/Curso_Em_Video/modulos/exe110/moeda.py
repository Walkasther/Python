from exe109 import moeda
from modulos.uteis import cabecalho

def resumo(numero, aumento, reducao, formatado=True):
    cabecalho('RESUMO DO VALOR')
    print(f'Preço analisado: \t{moeda.moeda(numero)}')
    print(f'Dobro do preço: \t{moeda.dobro(numero, formatado)}')
    print(f'Metade do preço: \t{moeda.metade(numero, formatado)}')
    print(f'{aumento}% de aumento: \t{moeda.aumentar(numero, aumento, formatado)}')
    print(f'{reducao}% de redução: \t{moeda.diminuir(numero, reducao, formatado)}')
    cabecalho()