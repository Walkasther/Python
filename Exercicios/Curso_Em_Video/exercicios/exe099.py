#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual é o maior.

from time import sleep

def maior(*valores):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in valores:
        sleep(0.25)
        print(valor, end=' ')
    print(f'\nForam passados {len(valores)} valores ao todo.')
    print(f'O Maior Valor informado foi {max(valores) if len(valores) > 0 else 0}.')


#Inicio do programa
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()