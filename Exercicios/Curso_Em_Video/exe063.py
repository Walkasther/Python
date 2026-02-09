#Escreva um programa que leia um número "n" inteiro qualquer e mostre na tela os "n" primeiros elementos de uma sequência
#de Fibonacci.
#ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
print(f'{'\033[36mSEQUENCIA DE FIBONACCI\033[m':-^50}')
n = int(input('Quantos números da sequencia quer mostrar? '))
c = 0
f1 = 0
f2 = 1
print('\033[32m%i,%d' % (f1,f2), end =',')
while c < n-2:
    f3 = f1 + f2
    print(f3, end=',' if c < n - 3 else '...')
    f1 = f2
    f2 = f3
    c += 1
