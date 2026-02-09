#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O Maior valor da segunda linha.

matriz = []
soma = 0
soma_terceira_coluna = 0
maior = 0
for cria_linha in range(3):
    linha = []
    for cria_coluna in range(3):
        linha.append(int(input(f'Informe o valor para [{cria_linha},{cria_coluna}]: ')))
    matriz.append(linha)

for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
for linha in range(3):
    for coluna in range (3):
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]
for c in range(3):
    soma_terceira_coluna += matriz[c][2]
for i,c in enumerate(matriz[1]):
    if i == 0:
        maior = c
    elif c > maior:
        maior = c

print(f'\033[32mA soma entre os valores pares é: {soma}')
print(f'\033[31mA soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'\033[33mO maior valor da segunda linha é: {maior}')
