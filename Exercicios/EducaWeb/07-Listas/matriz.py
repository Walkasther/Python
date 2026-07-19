matriz = [[int(input(f'digite o valor para [{i}:{j}]: ')) for j in range(3)] for i in range(3)]

print(matriz)
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end = '')
    print()