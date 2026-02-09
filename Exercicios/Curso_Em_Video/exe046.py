#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
#com uma pausa de um segundo entre eles.

from time import sleep

print('Contagem regressiva para o ano novo:')

for c in range (11, 0, -1):
    sleep(1)
    print(c - 1)

print('FELIZ ANO NOVO!\nFOGOS DE ARTIFICIO...')
