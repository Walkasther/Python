# Ler dois números M e N (máximo 10), e depois ler uma matriz MxN de números inteiros, conforme exemplo.
# Em seguida, mostrar na tela somente os números negativos da matriz.

m = int(input('Qual a quantidade de linhas da matriz? '))
n = int(input('Qual a quantidade de colunas da matriz? '))

matriz = []

for i in range(m):
    linha = []

    for j in range(n):
        linha.append(int(input(f'Elemento [{i},{j}]: ')))

    matriz.append(linha)

print('VALORES NEGATIVOS:')
for numeros in matriz:
    for numero in numeros:
        if numero < 0:
            print(numero)