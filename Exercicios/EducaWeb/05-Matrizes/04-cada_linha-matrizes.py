# Ler um inteiro N e uma matriz quadrada de ordem N (máximo = 10). Mostrar qual o maior elemento de cada linha.
# Suponha não haver empates.

n = int(input('Qual a ordem da matriz? '))

matriz = []

for i in range(n):
    linha = []

    for j in range(n):
        linha.append(int(input(f'Elemento [{i},{j}]: ')))
    matriz.append(linha)

print('MAIOR ELEMENTO DE CADA LINHA: ')
for numeros in matriz:
    print(max(numeros))