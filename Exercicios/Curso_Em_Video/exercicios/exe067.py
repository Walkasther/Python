#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.
print('-='*10)
print(f'{'TABUADA':*^20}')
print('-='*10)

n = 0
while True:
    n = int(input('\033[mDigite um número para ver a tabuada: '))
    if n < 0:
        break
    for c in range(0, 11):
        print(f'\033[33m{n:<5}\033[97mX\033[33m{c:^10}\033[97m=\033[32m{c*n:>5}')
    print('-' * 25)
print('Por enquanto é só, volte logo!')