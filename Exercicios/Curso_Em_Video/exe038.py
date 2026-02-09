#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#-O primeiro valor é maior
#-O segundo valor é maior
#-Não existe valor maior, os dois são iguais

n1 = input('Digite o primeiro valor: ')#dessa forma calcula até a posição das letras, qual letra é maior que a outra
n2 = input('Digite o segundo valor: ') #de acordo com a posição no alfabeto.

if n1 > n2: print(f'O primeiro valor {n1} é maior que o segundo valor {n2}')
elif n1 < n2: print(f'O segundo valor {n2} é maior que o primeiro valor {n1}')
else: print('Não existe valor maior, os dois valores são iguais!')
