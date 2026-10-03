# Faça um mini-sistema que utilize o Interactive Help do python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# obs: use cores

from Curso_Em_Video.Aulas.cores import  reset
from time import sleep

def titulo(t,cor='\033[42;97m'):
    linha = '~' * (len(t) + 4)
    print(cor, end='')
    print(linha)
    print(t.center(len(linha)))
    print(linha)

def ajuda_python(comando):
    titulo(f'Acessando o manual do comando {comando}', '\033[46;97m')
    sleep(1)
    print(f'\033[107;30m')
    help(comando)
    sleep(2)


while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando1 = input(f'{reset}Função ou Biblioteca > ')
    sleep(1)

    if comando1.lower() == 'fim':
        titulo('ATÉ LOGO!','\033[101;97m')
        break
    ajuda_python(comando1)