#Crie um programa que cie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.

# matriz = [[int(input(f'Digite um valor para [{y},{x}]: ')) for x in range(3)] for y in range(3)]
# print('-=' * 15)
# for i in range(0,3):
#     for j in range(0,3):
#         print(f'[ {matriz[i][j]} ]',end='' if j < 2 else '\n')

#Solução 2
matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0,3):
    for j in range(0,3):
        matriz2[i][j] = int(input(f'Digite o valor de [{i},{j}]: '))
for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz2[i][j]:^5}]', end='')
    print()