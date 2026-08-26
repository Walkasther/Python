#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='<Desconhecido>', gols=0):
    """
    pega o nome e a quantidade de gols que o jogador marcou e exibe a ficha do jogador
    :param nome: nome do jogador
    :param gols: quantidade de gols marcados
    :return: sem retorno
    """
    print(f'O jogador {nome} marcou {gols} gol(s) no campeonato')


jogador = input('Nome do jogador: ').strip()
n_gols = input('número de gols: ').strip()

if jogador and n_gols.isnumeric():
    ficha(jogador, int(n_gols))

elif jogador:
    ficha(jogador)

elif n_gols.isnumeric():
    ficha(gols= int(n_gols))

else:
    ficha()
