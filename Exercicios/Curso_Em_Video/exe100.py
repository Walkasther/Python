#Faça um programa que tenha uma lista chamada números e duas funções chamadas  sorteia() e somaPar(). A primeira
#função vai sortear 5 números e colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
#pares sorteados pela função anterior.

from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista:')
    for i in range(5):
        sleep(0.25)
        lista.append(randint(1,10))
        print(lista[-1], end=' ')
    print('PRONTO!')

def somaPar(valores):
    soma = sum(valor for valor in valores if valor % 2 == 0)
    print(f'Somando os valores pares de {valores}, temos {soma}')


#Inicio do programa
numeros = []

sorteia(numeros)
somaPar(numeros)