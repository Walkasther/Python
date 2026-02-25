#Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos
#serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import sample
from time import sleep
palpite = []
n = int(input('Quantos jogos quer que eu sorteie? '))
for i in range(0,n):
    sequencia = sorted(sample(range(1, 61),6))
    palpite.append(sequencia)
print(f'{'=' * 40}\n{'JOGOS DA MEGA SENA':^40}\n{'-'*40}')
print(f'{'-='*5}Sorteando {n} Jogos{'-='*5}')
for i, c in enumerate(palpite):
    sleep(1)
    print(f'JOGO {i + 1}: {c}')
print(f'{'-='*5} < BOA SORTE! > {'-='*5}')
