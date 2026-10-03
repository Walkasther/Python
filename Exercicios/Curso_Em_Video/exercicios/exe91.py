#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from Curso_Em_Video.Aulas.cores import verde, vermelho, azul, amarelo

jogadores = {'jogador1':randint(1,6),
             'jogador2':randint(1,6),
             'jogador3':randint(1,6),
             'jogador4':randint(1,6)}

for k, v in jogadores.items():
    print(f'{k} tirou {v}')
    sleep(1)

print('Ranking dos jogadores:')
n = 1

for k, v in sorted(jogadores.items(), key=lambda  item: item[1], reverse=True):
    if n == 1:
        print(verde, end='')
    elif n == 2:
        print(azul, end='')
    elif n == 3:
        print(amarelo, end='')
    else:
        print(vermelho, end='')

    print(f'{n}° lugar: {k} com {v}',)
    n += 1


