# Ler um inteiro N e uma matriz quadrada de ordem N (máximo = 10). Mostrar qual o maior elemento de cada linha.
# Suponha não haver empates.

n = int(input('Qual a ordem da matriz? '))

if 0 < n <= 10:
    matriz = []

    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(int(input(f'Elemento [{i},{j}]: ')))
        matriz.append(linha)

    print('MAIOR ELEMENTO DE CADA LINHA:')
    for linha in matriz:
        print(max(linha))
else:
    print('Valores invalidos')