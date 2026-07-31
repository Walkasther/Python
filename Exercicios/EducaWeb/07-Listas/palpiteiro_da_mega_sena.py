from random import sample
from time import sleep

numeros_sorteados = []
qtd_jogos = int(input('Quantos jogos você vai querer sortear? '))

print(f'{'-'* 30} \n{'JOGO DA MEGA SENA':^30} \n{'-' * 30}')
print(f'Sorteando {qtd_jogos} Sequências')

for i in range(qtd_jogos):
    numeros_sorteados.append(sorted(sample(range(1, 61), 6)))
    print(f'JOGO {i+1}: {numeros_sorteados[i]}')
    sleep(1)

print(f'{"-=" * 5} {"< BOA SORTE!>"} {"-=" * 5}')