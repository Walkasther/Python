#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
print('\033[107;30mRevelador de ano bissexto\033[m')
n= input('Digite o ano. [0] Para o ano atual: ')

if n =='0':
    ano = date.today().year
else:
    ano = int(n)

if n[-2:] == '00':
    bissexto = ano % 400
else:
    bissexto = ano % 4

if bissexto == 0:
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))