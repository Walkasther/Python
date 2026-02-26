# Ler uma matriz quadrada de ordem N (máximo = 10), contendo números reais. Em seguida, fazer as seguintes ações:
# A) calcular e imprimir a soma de todos os elementos positivos da matriz.
# B) fazer a leitura do índice de uma linha da matriz e, daí, imprimir todos os elementos desta linha.
# C) fazer a leitura de índice de uma coluna da matriz e, daí, imprimir todos os elementos desta coluna.
# D) imprimir os elementos da diagonal principal da matriz.
# E) alterar a matriz elevando ao quadrado todos os números negativos da mesma. Em seguida imprimir a matriz alterada.

n = int(input('Qual a ordem da matriz? '))

if 0 < n <= 10:
    matriz = []

    for i in range(n):
        linha = []

        for j in range(n):
            numero = float(input(f'Elemento [{i},{j}]: '))
            linha.append(numero)
        matriz.append(linha)

    soma = 0
    for i in range(n):
        for j in range(n):
            if matriz[i][j] > 0:
                soma += matriz[i][j]

    print(f'SOMA DOS POSITIVOS: {soma}')

    escolha_linha = int(input('Escolha uma linha: '))
    print('LINHA ESCOLHIDA:', end='')
    for valor in matriz[escolha_linha]:
        print(valor, end=' ')
    print()

    escolha_coluna = int(input('Escolha uma coluna: '))
    print('COLUNA ESCOLHIDA:', end=' ')
    for i in range(n):
        print(matriz[i][escolha_coluna], end=' ')
    print()

    print('DIAGONAL PRINCIPAL:', end='')
    for i in range(n):
        print(matriz[i][i], end=' ')
    print()

    print('MATRIZ ALTERADA:')
    for i in range(n):
        for j in range(n):
            if matriz[i][j] < 0:
                matriz[i][j] = matriz[i][j] ** 2
            print(matriz[i][j], end=' ')
        print()
else:
    print('Valores invalidos')