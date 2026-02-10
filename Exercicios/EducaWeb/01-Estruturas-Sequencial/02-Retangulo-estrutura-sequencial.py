#Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor da área,
# perímetro e diagonal deste retângulo, com quatro casas decimais.

from math import sqrt

base = float(input('Qual a base do retângulo? '))
altura = float(input('Qual a altura do retângulo? '))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = sqrt(base ** 2 + altura ** 2)

print(f'\033[31mÁrea: {area:.4f}\n\033[32mPerímetro: {perimetro:.4f}\n\033[33mDiagonal: {diagonal:.4f}')
