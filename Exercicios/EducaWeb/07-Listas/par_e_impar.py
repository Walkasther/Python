valores = []
valores_pares = list()
valores_impares = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = int(input('\033[30;44mQuer continuar? [1]Sim [0]Não:\033[m'))

    if continuar == 0:
        break

for valor in valores:
    if valor % 2 == 0:
        valores_pares.append(valor)
    else:
        valores_impares.append(valor)

print(f'\033[33mLista com os valores digitados: {valores}')
print(f'\033[31mLista dos pares: {valores_pares}')
print(f'\033[32mLista dos impares: {valores_impares}')