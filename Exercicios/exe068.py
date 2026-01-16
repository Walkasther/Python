#Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER,
#mostrando o total de vitórias que consecutivas que ele conquistou no final do jogo.

from random import randint
c = 0
vencedor = 'jogador'
escolha = 0
jogador = 0
print(f'{'Jogo do par ou impar':-^50}')
while True:
    computador = randint(0, 10)
    print('-' * 50)
    while escolha not in [1,2]:
        escolha = int(input('[1]IMPAR OU [2]PAR: '))
    jogador = int(input('Escolha um número: '))
    print(f'Escolhido pelo computador: {computador}')
    resultado = jogador + computador
    if resultado % 2 == 0:
        print('Deu par!')
        print('Você ' + ('ganhou!' if escolha == 2 else 'perdeu.'))
        vencedor = 'computador' if escolha == 1 else 'jogador'
        escolha = 0
    else:
        print('Deu impar!')
        print('Você ' + ('ganhou!' if escolha == 1 else 'perdeu.'))
        vencedor = 'computador' if escolha == 2 else 'jogador'
        escolha = 0
    if vencedor == 'computador':
        break
    else:
        c += 1
if c == 0:
    print('Perdeu de primeira kkk')
else:
    print(f'Parabéns, Você ganhou {c} vezes.')