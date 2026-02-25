# Fazer um programa para ler dois números inteiros M e N (máximo 10). Em seguida, ler uma matriz de M linhas e N
# colunas contendo números reais. Gerar um vetor de modo que cada elemento do vetor seja a soma dos elementos da
# linha correspondente da matriz. Mostrar o vetor gerado.

m = int(input('Qual a quantidade de linhas da matriz? '))
n = int(input('Qual a quantidade de colunas da matriz? '))

matriz = []

for i in range(m):
    matriz.append([])
    print(f'Digite os elementos da {i+1}a. linha: ')
    for j in range(n):
        matriz[i].append(float(input()))

vetor = []

for i in range(m):
    vetor.append(sum(matriz[i]))


print('VETOR GERADO:')
for resultado in vetor:
    print(f'{resultado}')