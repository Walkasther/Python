# Fazer um programa para ler um número inteiro N (máximo 10) e uma matriz quadrada de ordem N contendo números inteiros.
# Em seguida, mostrar a diagonal principal e a quantidade de valores negativos da matriz.

n = int(input('Qual a ordem da matriz? '))
quantidade_negativos = 0

matriz = [[int(input(f'Elemento [{i},{j}]: ')) for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if matriz[i][j] < 0:
            quantidade_negativos += 1
        if i == j:
            print(f'{matriz[i][j]}', end='\n' if i+1 == n and j+1 == n else ' ')

print(f'QUANTIDADE DE NEGATIVOS = {quantidade_negativos}')

