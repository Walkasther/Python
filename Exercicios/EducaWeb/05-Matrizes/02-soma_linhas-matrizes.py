# Fazer um programa para ler dois números inteiros M e N (máximo 10). Em seguida, ler uma matriz de M linhas e N
# colunas contendo números reais. Gerar um vetor de modo que cada elemento do vetor seja a soma dos elementos da
# linha correspondente da matriz. Mostrar o vetor gerado.

m = int(input('Qual a quantidade de linhas da matriz? '))
n = int(input('Qual a quantidade de colunas da matriz? '))

if (0 < m <= 10) and (0 < n <= 10):
    matriz = []

    for i in range(m):
        print(f'Digite os elementos da {i+1}a. linha: ')
        linha = []
        for j in range(n):
            linha.append(float(input()))
        matriz.append(linha)

    vetor = []
    for linha in matriz:
        vetor.append(sum(linha))


    print('VETOR GERADO:')
    for resultado in vetor:
        print(f'{resultado:.1f}')
else:
    print('Valores invalidos')