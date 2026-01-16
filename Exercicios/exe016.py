# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: (Digite um número: 6.127) resposta esperada: O número 6.127 tem a parte inteira 6.

from math import floor, trunc

numero = input('\033[32mDigite um número: ')
n1 = float(numero)
#solução 1
print('\033[91m')
print('A parte inteira de {} é {}'.format(n1,int(n1)))
#solução 2
print('A parte inteira de {} é {}'.format(n1, floor(n1)))
#solução 3
print('A parte inteira de {} é {}'.format(n1, trunc(n1)))