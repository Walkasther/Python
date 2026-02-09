#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# n = int(input('Digite um número inteiro: '))
# primo = False
# if n <= 2:
#     if n == 2:
#         print('\033[32mEsse é um número primo!')
#     elif n == 1:
#         print('\033[35mO número 1 não é considerado primo nem composto, pois possui apenas um divisor!')
#     elif n == 0:
#         print('\033[34mO número 0 não é primo nem composto, pois possui infinitos divisores!')
#     else:
#         print('\033[36mLamento, más não existem números primos negativos!')
# else:
#     for i in range (2,n):
#         primo =  False if n % i == 0 else True
#         if not primo:
#             break
#     if primo:
#         print('\033[32mEsse é um número primo!')
#     else:
#         print('\033[31mEsse não é um número primo')

#########################################################
num = int(input('digite um numero inteiro: '))
tot = 0
for i in range (1,num+1):
    if num % i == 0:
        print('\033[31m',end='')
        tot += 1
    else:
        print('\033[33m',end='')
    print('%i' % i, end=' ')
print('\n\033[34mO número %d possui %i divisores, portanto, ele' % (num, tot),end=' ')
if tot == 2:
    print('\033[32mé um número primo. :)')
else:
    print('\033[31mnão é um número primo. :(')
