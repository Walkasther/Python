#crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.

n = input('\033[101;97mDigite um número: \033[m')
n2 = int(n)
if n2 % 2 == 0:
    print('O número digitado é par')
else:
    print('O numero digitado é impar')