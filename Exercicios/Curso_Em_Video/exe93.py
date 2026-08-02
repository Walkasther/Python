#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler a quantidade de gols feitos
#em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.



from Curso_Em_Video.Aulas.cores import cores_claras

linha = '\033[m' + ('-=' * 30)
nome = input('Nome do jogador: ')
partidas_jogadas = int(input(f'Quantas partidas {nome} jogou? '))

jogador = {'nome': nome, 'gols': []}

for i in range(partidas_jogadas):
    jogador['gols'].append(int(input(f'{cores_claras[i % len(cores_claras)]}Quantos gols na partida {i + 1}: ')))

jogador['total'] = sum(jogador['gols'])

print(linha)
print(jogador)
print(linha)

for i, (k, v) in enumerate(jogador.items()):
    print(f'{cores_claras[i % len(cores_claras)]}O campo {k} tem o valor {v}.\033[m')
print(linha)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, gols in enumerate(jogador['gols']):
    print(f'{cores_claras[i % len(cores_claras)]}    => Na partida {i+1}, fez {gols} gol(s).\033[m')
print(f'Foi um total de {jogador["total"]} gol(s)')