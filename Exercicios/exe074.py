#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
#números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

tupla_numeros_aleatorios = randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)
maior = 0
menor = 0
print(f'Os valores sorteados foram: ', end=' ')

for n,c in enumerate(tupla_numeros_aleatorios):
    print(c,end =' ' if n+1 < len(tupla_numeros_aleatorios) else '\n' )
    if n == 0:
        maior = c
        menor = c
    else:
        if maior < c:
            maior = c
        elif menor > c:
            menor = c
print(f'\033[34mO Maior valor sorteado foi: {maior}')
print(f'\033[33mO menor valor sorteado foi {menor}')
