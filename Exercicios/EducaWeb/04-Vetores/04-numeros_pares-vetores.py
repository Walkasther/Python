# Faça um programa que leia N números inteiros e armazene-os em um vetor. Em seguida, mostre na
# tela todos os números pares, e também a quantidade de números pares.

n = int(input('Quantos numeros voce vai digitar? '))
numeros = []
tot_par = 0

for _ in range(n):
    numeros.append(int(input('Digite um numero: ')))

print('NUMEROS PARES:')

for i in numeros:
    if i % 2 == 0:
        print(i, end=' ')
        tot_par += 1
print(f'\nQuantidade de pares = {tot_par}')