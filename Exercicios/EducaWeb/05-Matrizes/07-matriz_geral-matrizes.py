# Ler uma matriz quadrada de ordem N (máximo = 10), contendo números reais. Em seguida, fazer as seguintes ações:
# A) calcular e imprimir a soma de todos os elementos positivos da matriz.
# B) fazer a leitura do índice de uma linha da matriz e, daí, imprimir todos os elementos desta linha.
# C) fazer a leitura de índice de uma coluna da matriz e, daí, imprimir todos os elementos desta coluna.
# D) imprimir os elementos da diagonal principal da matriz.
# E) alterar a matriz elevando ao quadrado todos os números negativos da mesma. Em seguida imprimir a matriz alterada.

n = int(input('Qual a ordem da matriz? '))

soma = 0
matriz = []

for i in range(n):
    linha = []

    for j in range(n):
        numero = float(input(f'Elemento [{i},{j}]: '))
        linha.append(numero)
        if numero > 0:
            soma += numero
    matriz.append(linha)

print(f'\nSOMA DOS POSITIVOS: {soma}')
print()

escolha_linha = int(input('Escolha uma linha: '))

print('LINHA ESCOLHIDA:', end='')
for valor in matriz[escolha_linha]:
    print(valor, end=' ')
print()

escolha_coluna = int(input('\nEscolha uma coluna: '))

print('COLUNA ESCOLHIDA:', end=' ')
for i in range(n):
    print(matriz[i][escolha_coluna], end=' ')
print()

print('\nDIAGONAL PRINCIPAL:', end='')
for i in range(n):
    for j in range(n):
        if i == j:
            print(matriz[i][j], end=' ')
print()

print('\nMATRIZ ALTERADA:')
for i in range(n):
    for j in range(n):
        if matriz[i][j] < 0:
            matriz[i][j] = matriz[i][j] ** 2

        print(matriz[i][j], end=' ')
    print()