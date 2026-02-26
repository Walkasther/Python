# Ler um inteiro N (máximo 10) e uma matriz quadrada de ordem N contendo números inteiros. Mostrar a soma dos
# elementos acima da diagonal principal.

n = int(input('Qual a ordem da matriz? '))

soma = 0
matriz = []

for i in range(n):
    linha = []

    for j in range(n):
        linha.append(int(input(f'Elemento [{i},{j}]: ')))
        if i < j:
            soma += linha[j]

    matriz.append(linha)

print(f'SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = {soma}')