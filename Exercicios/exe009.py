#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
from cores import verde_claro

n = int(input('{}Digite um número inteiro: '.format(verde_claro)))
print('\033[0;34m=' * 5 + ' Tabuada do {} '.format(n) + '=' * 5)
print('\033[33m')
print('{:>6}  * {:>2} = {}'.format(1, n, n * 1))
print('{:>6}  * {:>2} = {}'.format(2, n, n * 2))
print('{:>6}  * {:>2} = {}'.format(3, n, n * 3))
print('{:>6}  * {:>2} = {}'.format(4, n, n * 4))
print('{:>6}  * {:>2} = {}'.format(5, n, n * 5))
print('{:>6}  * {:>2} = {}'.format(6, n, n * 6))
print('{:>6}  * {:>2} = {}'.format(7, n, n * 7))
print('{:>6}  * {:>2} = {}'.format(8, n, n * 8))
print('{:>6}  * {:>2} = {}'.format(9, n, n * 9))
print(' {:>6} * {:>2} = {}'.format(10, n, n * 10))