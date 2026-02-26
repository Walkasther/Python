# Fazer um programa para ler duas matrizes de números inteiros A e B, contendo de M linhas e N colunas cada (M e N máximo 10).
# Depois, gerar uma terceira matriz C onde cada elemento desta é a soma dos elementos correspondentes das matrizes originais.
# Imprimir na tela a matriz gerada.

m = int(input('Quantas linhas vai ter cada matriz? '))
n = int(input('Quantas colunas vai ter cada matriz? '))

if 0 < m <= 10 and 0 < n <= 10:
    matriz_a = []
    matriz_b = []
    matriz_c = []

    for a in range(3):
        matriz_atual = matriz_a if a == 0 else matriz_b if a == 1 else matriz_c
        nome = 'A' if a == 0 else 'B'

        print(f'Digite os valores da matriz {nome}:')

        for i in range(m):
            linha = []
            for j in range(n):
                if a == 0 or a == 1:
                    linha.append(int(input(f'Elemento [{i},{j}]: ')))
                else:
                    linha.append(matriz_a[i][j] + matriz_b[i][j])
            matriz_atual.append(linha)

    print('MATRIZ SOMA:')
    for linha in matriz_c:
        for numero in linha:
            print(numero, end=' ')
        print()
else:
    print('Valores invalidos')
