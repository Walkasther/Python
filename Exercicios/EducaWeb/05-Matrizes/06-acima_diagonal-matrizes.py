# Ler um inteiro N (máximo 10) e uma matriz quadrada de ordem N contendo números inteiros. Mostrar a soma dos
# elementos acima da diagonal principal.

n = int(input('Qual a ordem da matriz? '))

if 0 < n <= 10:
    matriz = []

    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(int(input(f'Elemento [{i},{j}]: ')))
        matriz.append(linha)

    soma = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                soma += matriz[i][j]

    print(f'SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = {soma}')

else:
    print('Valores invalidos')
