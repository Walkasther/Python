#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for i in range (0,5):
    peso = float(input('Informe o peso da %i° pessoa: ' % (i + 1)))
    if i == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('\033[33mO maior peso é %.2f \033[34me o menor peso é %.2f' % (maior, menor))
