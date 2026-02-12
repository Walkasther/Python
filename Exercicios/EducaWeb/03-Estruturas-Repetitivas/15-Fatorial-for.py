# Fazer um programa para ler um número natural N (valor máximo: 15), e depois calcular e mostrar o
# fatorial de N.

n = int(input('Digite o valor de N. (Max: 15): '))

if 0 <= n <= 15:
    fatorial = 1

    for i in range(1,n+1):
        fatorial *= i

    print(f'FATORIAL = {fatorial}')

else:
    print('Valor inválido')