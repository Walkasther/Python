# Crie um programa que tenha uma função fatorial() que receba dois parametros: o primeiro que indique o número e o outro
# que será um valor lógico(opcional), indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(x, show=False):
    """
    \033[31mFunção que calcula o fatorial de um número.
    \033[33m:param x: Rebebe um número inteiro para calcular o fatorial
    \033[33m:param show: Parâmetro opcional, recebe um valor lógico. Se True, mostra o processo de cálculo fatorial
    \033[92m:return: Retorna o fatorial do número analisado
    """
    resultado = 1
    print('-' * 30)
    for i in range(x,0,-1):
        resultado *= i
        if show:
            print(i,end=' x ' if i > 1 else ' = ')


    return resultado

print(fatorial(5, True))

help(fatorial)
