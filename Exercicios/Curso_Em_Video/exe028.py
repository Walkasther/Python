#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
#descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário ganhou ou perdeu.

from random import randint
from time import sleep

n = randint(0,5)
print('\033[103;36m-=-' * 10)
e = int(input('\033[0;33mEm qual número estou pensando? '))
print('\033[103;36m-=-' * 10)
print('\033[0mPROCESSANDO...')
sleep(2)
if e == n:
    print('Parabéns, você acertou! eu pensei no número {}'.format(n))
else:
    print('HEHE eu Ganhei e você perdeu. O número que eu pensei foi {}'.format(n))
