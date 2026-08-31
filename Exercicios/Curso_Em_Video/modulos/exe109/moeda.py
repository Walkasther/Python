from modulos.moeda_base import (metade as _metade,
                                dobro as _dobro,
                                diminuir as _diminuir,
                                aumentar as _aumentar)
from modulos.exe108.moeda import moeda

def aumentar(numero, aumento, formatado=False):
    valor = _aumentar(numero, aumento)

    if formatado:
        valor = moeda(valor)

    return valor


def diminuir(numero, reducao, formatado=False):
    valor = _diminuir(numero, reducao)

    if formatado:
        valor = moeda(valor)

    return valor

def dobro(numero, formatado=False):
    valor = _dobro(numero)

    if formatado:
        valor = moeda(valor)

    return valor

def metade(numero, formatado=False):
    valor = _metade(numero)

    if formatado:
        valor = moeda(valor)

    return valor