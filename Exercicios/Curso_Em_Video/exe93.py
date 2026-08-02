#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler a quantidade de gols feitos
#em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.



from Curso_Em_Video.Aulas.cores import cores_claras

cores = cores_claras.copy()
cores_reset = cores_claras.copy()

linha = '\033[m-=' * 30
nome = input('Nome do jogador: ')
partidas_jogadas = int(input(f'Quantas partidas {nome} jogou? '))

jogador = {'nome': nome, 'gols': []}

for i in range(partidas_jogadas):
    if len(cores) == 0:
        cores = cores_reset[:]
    print(cores[-1],end = '')
    jogador['gols'].append(int(input(f'Quantos gols na partida {i + 1}: ')))
    cores.pop()

jogador['total'] = sum(jogador['gols'])

print(linha)
print(jogador)
print(linha)

for k, v in jogador.items():
    if len(cores) == 0:
        cores = cores_reset[:]

    print(cores[0],end='')
    print(f'O campo {k} tem o valor {v}.')

    cores.pop(0)
print(linha)
cores = cores_reset[:]

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, gols in enumerate(jogador['gols']):
    if len(cores) == 0:
        cores = cores_reset[:]
    print(cores[-1],end='')
    print(f'    => Na partida {i+1}, fez {gols} gols.')
    cores.pop()

print(f'\033[mFoi um total de {jogador["total"]} gols')