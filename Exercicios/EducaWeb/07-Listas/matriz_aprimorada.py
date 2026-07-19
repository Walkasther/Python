matriz = []
soma_par = soma_terceira_coluna = 0

for i in range(3):
    matriz.append([])
    for j in range(3):
        matriz[i].append(int(input(f'Digite um numero para [{i}:{j}]: ')))

for linha in matriz:
    for coluna in linha:
        print(f'\033[30;44m[{coluna:^5}]', end='\033[m')
    print()

for linha in matriz:
    for coluna in linha:
        if coluna % 2 == 0:
            soma_par += coluna

for linha in matriz:
    soma_terceira_coluna += linha[2]


print(f'\033[33mA soma dos valores pares digitados é: {soma_par}')
print(f'\033[36mA soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'\033[35mO maior valor da segunda linha é: {max(matriz[1])}')