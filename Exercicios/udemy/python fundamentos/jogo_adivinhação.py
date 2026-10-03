from exercicios.modulos import print_formatado, leia_int
from random import randint

x = randint(0,50)

print_formatado('Vamos ver se você adivinha o número que escolhi!', 'ciano')

for i in range(10,0,-1):
    print_formatado(f'Você tem {i} tentativas!', tipo='aviso')

    escolha = leia_int('Escolha um número entre 0 e 50: ', cor=True, minimo=0, maximo=50)

    media = (escolha + x) / 2

    if escolha > x:
        dica = 'abaixo'

    elif escolha < x:
        dica = 'acima'

    else:
        print_formatado(f'PAREBÉNS!!! Você acertou, o número que eu pensei foi justamente o {escolha}', tipo='sucesso')
        break


    if escolha >= media:
        temperatura = 'frio'
        cor = 'azul'
        fundo = 'preto'

    else:
        temperatura = 'quente'
        cor = 'vermelho'
        fundo = 'preto'

    if i == 1:
        print_formatado(f'Lamento, más você não acertou e suas tentativas acabaram. \nO número que eu pensei foi o {x}', tipo='destaque')
    else:
        print_formatado(f'Você está {temperatura}!  O número que eu escolhi está {dica} do {escolha}', cor, fundo=fundo)