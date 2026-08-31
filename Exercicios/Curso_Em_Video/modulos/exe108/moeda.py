from modulos.moeda_base import metade, dobro, diminuir, aumentar

def moeda(valor):
    return f"R${valor:.2f}".replace('.',',')