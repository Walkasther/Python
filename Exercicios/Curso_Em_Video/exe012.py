# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

n = float(input('Qual o preço do produto?'))
print('\033[97mO novo preço do produto é: R${:.2f}'.format(n - n * 0.05))