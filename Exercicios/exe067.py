#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.
print('-='*10)
print(f'{'TABUADA':*^20}')
print('-='*10)

n = 0
while True:
    c = 0
    n = int(input('\033[mDigite um número para ver a tabuada: '))
    if n < 0:
        break
    while c <= 10:
        print(f'\033[33m{n:<5}\033[mX\033[33m{c:^10}\033[m=\033[32m{c*n:>5}')
        c += 1
        print('-' * 25)
print('Por enquanto é só, volte logo!')