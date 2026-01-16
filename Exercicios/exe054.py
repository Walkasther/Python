#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
#maioridade e quantas já são maiores. Considere a maioridade sendo 21 anos.
from datetime import date
maior = 0
menor = 0
ano_atual = date .today().year
print(ano_atual)
for i in range (0,7):
    idade = ano_atual - int(input('Informe o ano de nascimento da %d° pessoa: ' % (i+1)))
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Das 7 pessoas,\033[32m %i já atingiram a maior idade, \033[31menquanto %d ainda não atingiram a maior idade.' % (maior, menor))
