#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
#No final, mostre:
#A) Qual é o total gasto na compra.
#B) Quantos produtos custam mais de R$ 1000.
#C) Qual é o nome do produto mais barato.

total = mais_1000 = preco_mais_barato = 0
c = 1
nome_mais_barato = str
while True:
    print('=' * 30)
    nome = input(f'Informe o nome do {c}° produto: ')
    preco = float(input(f'Informe o preço do {c}° produto: R$'))
    print('=' * 30)
    continuar = int(input('Quer continuar? [1]SIM [2]NÃO: '))
    total += preco
    if preco > 1000:
        mais_1000 += 1
    if c == 1 or preco_mais_barato > preco:
        nome_mais_barato = nome
        preco_mais_barato = preco
    if continuar == 1:
        c += 1
    else:
        break
print(f'Total da compra: R${total:.2f}')
print(f'Quantidade de Produtos que custam mais de R$1000: {mais_1000}')
print(f'Produto mais barato: {nome_mais_barato} custando R${preco_mais_barato:.2f}')
