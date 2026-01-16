#Crie um programa que faça o computador jogar jokenpô com você.

from random import randint
from time import sleep

#0-Pedra 1-Papel 3-Tesoura
escolha_computador = randint(0,2)
escolha_computador2 = 'Pedra' if escolha_computador == 0 else 'Papel' if escolha_computador == 1 else 'Tesoura'

escolha_pessoa = int(input('Informe o número correspondente a sua escolha: \033[31m0-Pedra  \033[32m1-Papel  \033[33m2-Tesoura: '))
escolha_pessoa2 = 'Pedra' if escolha_pessoa == 0 else 'Papel' if escolha_pessoa == 1 else 'Tesoura'

if escolha_pessoa <= 2:

    sleep(0.5)
    print('\033[97mJO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!')
    sleep(0.5)
    print('\033[95mEscolha do computador: {}'.format(escolha_computador2))

    print('\033[36m=-' * 40)
    if escolha_computador == escolha_pessoa:
        print(f'\033[33mEmpatamos, eu também escolhi {escolha_computador2}')
    elif ((escolha_computador == 0 and escolha_pessoa == 2) or
         (escolha_computador == 1 and escolha_pessoa == 0) or
         (escolha_computador == 2 and escolha_pessoa == 1)):
            print(f'\033[91mHEHE EU VENCI!!! Você jogou {escolha_pessoa2} e eu joguei {escolha_computador2}')
    else:
        print(f'\033[92mPARABENS, VOCÊ GANHOU!!! Você jogou {escolha_pessoa2} e eu joguei {escolha_computador2}')
    print('\033[36m=-' * 40)
else:
    print('\033[107;30mJOGADA INVÁLIDA!!\033[m')
