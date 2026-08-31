from modulos.uteis import cabecalho


def aumentar(numero, aumento, formatado=False):
    valor = numero + (numero * aumento / 100)

    if formatado:
        valor = moeda(valor)

    return valor


def diminuir(numero, reducao, formatado=False):
    valor = numero - (numero * reducao / 100)

    if formatado:
        valor = moeda(valor)

    return valor


def dobro(numero, formatado=False):
    valor = numero * 2

    if formatado:
        valor = moeda(valor)

    return valor


def metade(numero, formatado=False):
    valor = numero / 2

    if formatado:
        valor = moeda(valor)

    return valor


def moeda(valor):
    return f"R${valor:.2f}".replace('.',',')


def resumo(numero, aumento, reducao, formatado=True):
    cabecalho('RESUMO DO VALOR')
    print(f'{"Preço analisado:":<20}{moeda(numero)}')
    print(f'{"Dobro do preço:":<20}{dobro(numero, formatado)}')
    print(f'{"Metade do preço:":<20}{metade(numero, formatado)}')
    print(f'{f"{aumento}% de aumento:":<20}{aumentar(numero, aumento, formatado)}')
    print(f'{f"{reducao}% de redução:":<20}{diminuir(numero, reducao, formatado)}')
    cabecalho()
