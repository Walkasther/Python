# Fazer um programa para ler dois números inteiros, e dizer se um número é múltiplo do outro. Os números podem ser
# digitados em qualquer ordem.

print('Digite dois números inteiros:')
n_1 = int(input())
n_2 = int(input())

if n_1 % n_2 == 0 or n_2 % n_1 == 0:
    print('São múltiplos')
else:
    print('Não são múltiplos')
