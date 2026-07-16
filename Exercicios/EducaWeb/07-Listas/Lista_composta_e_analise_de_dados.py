pessoas = [['Mateus',88], ['Lucas',88], ['Maria',40], ['Aline', 40], ['Paulo', 58]]
maior = menor = qmaior = qmenor = 0

while True:
    dados = [input('Digite o nome: '), int(input('Digite o peso: '))]
    pessoas.append(dados[:])
    dados.clear()
    continuar = int(input('\033[30;44mQuer Continuar? [1]Sim [0]Não:\033[m'))

    if continuar == 0:
        break

for qtd, pessoa in enumerate(pessoas):
    if qtd == 0:
        maior = menor = pessoa[1]
        qmaior = qmenor = 1
    elif pessoa[1] > maior:
        maior = pessoa[1]
        qmaior = 1
    elif pessoa[1] < menor:
        menor = pessoa[1]
        qmenor = 1
    elif pessoa[1] == maior:
        qmaior += 1
    elif pessoa[1] == menor:
        qmenor += 1

print(f'Foram cadastradas {len(pessoas)} Pessoas')

print(f'\033[35mAs pessoas mais pesadas são:' if qmaior > 1 else 'A pessoa mais pesada é:')
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f'{pessoa[0]} com {pessoa[1]} Kilos')

print(f'\033[33mAs pessoas mais leves são:' if qmenor > 1 else 'A pessoa mais leve é:')
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f'{pessoa[0]} com {pessoa[1]} Quilos')