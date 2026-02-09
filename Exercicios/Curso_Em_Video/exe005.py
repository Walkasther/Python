# Faça um programa que leia um número inteiro, e mostre na tela o seu sucessor e o seu antecessor

n1 = int(input('\033[97mDigite um número: '))
print('\033[91;107mO sucessor de {} é {} e o seu antecessor é: {}\033[m'.format(n1,n1+1,n1-1))
