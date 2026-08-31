from modulos.moeda_base import (metade as _metade, dobro as _dobro, diminuir as _diminuir, aumentar as _aumentar)
from modulos.exe108.moeda import moeda


def aumentar(numero, aumento, formatado=False):
    valor = _aumentar(numero, aumento)
    return valor if not formatado else moeda(valor)


def diminuir(numero, reducao, formatado=False):
    valor = _diminuir(numero, reducao)
    return moeda(valor) if formatado else valor


def dobro(numero, formatado=False):
    valor = _dobro(numero)
    return moeda(valor) if formatado else valor


def metade(numero, formatado=False):
    valor = _metade(numero)
    return moeda(valor) if formatado else valor
