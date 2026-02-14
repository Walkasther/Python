# Faça um programa que leia um número inteiro positivo N (máximo = 10) e depois N números inteiros
# e armazene-os em um vetor. Em seguida, mostrar na tela todos os números negativos lidos.

n = int(input('Quantos numeros voce vai digitar? '))
valores = []

if 0 <= n <= 10:
    for _ in range(n):
        valores.append(int(input('Digite um numero: ')))

    print('NUMEROS NEGATIVOS:')

    for i in valores:
        if i < 0:
            print(i)

else:
    print('Valor invalido!')