#Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
dados = []
pessoas = []
while True:
    dados.append(input('Nome:'))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    continuar = input('Quer continuar? [S]SIM [N]NÃO: ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')

maior = menor = 0
for i,c in enumerate(pessoas):
    if i == 0:
        maior = c[1]
        menor = c[1]
    else:
        if c[1] >= maior:
            maior = c[1]
        elif c[1] <= menor:
            menor = c[1]
print(f'o maior peso cadastrado foi de {maior} KG de ')
for c in pessoas:
    if c[1] == maior:
        print(c[0], end=', ')
print(f'\nO menor peso cadastrado foi de {menor}Kg de ')
for c in pessoas:
    if c[1] == menor:
        print(c[0], end=', ')
