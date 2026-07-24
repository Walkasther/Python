pessoas = []

while True:
    dados = [input('Digite o nome: '), float(input('Digite o peso: '))]
    pessoas.append(dados[:])
    continuar = int(input('\033[30;44mQuer Continuar? [1]Sim [0]Não:\033[m'))

    if continuar == 0:
        break

maior = menor = pessoas[0][1]

for pessoa in pessoas[1:]:
    if pessoa[1] > maior:
        maior = pessoa[1]
    elif pessoa[1] < menor:
        menor = pessoa[1]

print(f'Foram cadastradas {len(pessoas)} Pessoas')

print(f'\033[35mAs pessoas mais pesadas são:')
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f'{pessoa[0].capitalize()} com {pessoa[1]} Kilos')

print(f'\033[33mAs pessoas mais leves são:')
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f'{pessoa[0].capitalize()} com {pessoa[1]} Quilos')