# Fazer um programa para ler os três coeficientes de uma equação do segundo grau. Usando a fórmula
# de Bhaskara, calcular e mostrar os valores das raízes x1 e x2 da equação com quatro casas decimais,
# conforme exemplo. Se a equação não possuir raízes reais, mostrar uma mensagem.

from math import sqrt

a = float(input('Coeficiente a: '))
b = float(input('Coeficiente b: '))
c = float(input('Coeficiente c: '))

if a == 0:
    print('Essa não é uma equação do segundo grau.')
else:
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print('Esta equação não possui raízes reais.')
    else:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)

        print(f'X1 = {x1:.4f}')
        print(f'X2 = {x2:.4f}')
