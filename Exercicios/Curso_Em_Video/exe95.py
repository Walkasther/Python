# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador.

jogadores = []

while True:
    jogador = dict(nome = input('Nome do jogador: '),
                   gols = [])
    partidas_jogadas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(partidas_jogadas):
        jogador['gols'].append(int(input(f'Quantos gols na partida {i+1}? ')))

    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador)
    continuar = input('\033[44;30mQuer continuar? [S]im | [N]ão:\033[m ').strip().upper()[0]

    if continuar == 'N':
        break

print('-=' * 30)
print(f'{"cod":<10}{"nome":<10}{"Gols":<20}{"Total":<10}')
print('-' * 60)

for i, jogador in enumerate(jogadores):
    print(f'{i:<10}{jogador["nome"]:<10}{", ".join(map(str, jogador["gols"])):<20}{jogador["total"]:<10}')

while True:
    print('-' * 60)
    exibir_dados = int(input('Mostrar dados de qual jogador? (999 interrompe): '))

    if exibir_dados == 999:
        break

    elif (exibir_dados < 0) or exibir_dados >= len(jogadores):
        print(f'\033[91mERRO! Não existe jogador com o código {exibir_dados}! Tente novamente\033[m')

    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[exibir_dados]["nome"]}')
        for i, gols in enumerate(jogadores[exibir_dados]['gols']):
            print(f'   No jogo {i+1} fez {gols} gol(s)')

print('<< VOLTE SEMPRE >>')