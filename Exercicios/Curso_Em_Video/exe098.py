#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo. E realize a contagem
#Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada.

from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    if inicio > fim and passo > 0:
        passo = -passo

    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} contando de {abs(passo)} em {abs(passo)}')

    if inicio > fim:
        fim -= 2
    for j in range(inicio, fim+1, passo):
        sleep(0.25)
        print(j, end=' ')
    print('FIM!')


#Inicio do programa:
contador(1, 10, 1)
contador(10, 0, -2)

print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')

contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))