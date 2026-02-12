# Escreva um algoritmo que leia dois números e imprima o resultado da divisão do primeiro pelo
# segundo. Caso não for possível, mostre a mensagem “DIVISÃO IMPOSSÍVEL”.

n = int(input('Quantos casos voce vai digitar? '))

for _ in range(n):
    n_1 = int(input('Entre com o numerador: '))
    n_2 = int(input('Entre com o denominador: '))

    if n_2 == 0:
        print('DIVISÃO IMPOSSÍVEL')
    else:
        print(f'DIVISÃO = {n_1 / n_2}')