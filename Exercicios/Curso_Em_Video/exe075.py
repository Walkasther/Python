#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
from itertools import count

tupla_a = int(input('Valor1:')), int(input('Valor2:')), int(input('Valor3:')), int(input('Valor4:'))
p = 0
print(f'O número 9 apareceu {tupla_a.count(9)} vezes.')
if tupla_a.count(3) > 0: print(f'O número 3 aparece pela primeira vez na {tupla_a.index(3)+1}° posição.')
else: print('O valor 3 não foi digitado em nenhuma posição')
for c in tupla_a:
    if c % 2 == 0:
        p = 1

if p == 1:
    print(f'Os números pares digitados foram: ', end='')
    for c in tupla_a:
        if c % 2 == 0: print(c, end=' ')
else: print('Não foram digitados valores pares')