#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#ex: 5! = 5x4x3x2x1 = 120

n = int(input('Digite um número: '))
c = n - 1
resultado = n
print('\033[33m', end = '')
print(n,end=' \033[97mx ')
while c != 0:
    resultado *= c
    print('\033[33m%d' % c, end = ('\033[97m x \033[m' if c != 1 else '\033[32m = \033[m'))
    c -= 1
print(resultado)
print('\033[36mO fatorial de %i é %d' % (n, resultado))