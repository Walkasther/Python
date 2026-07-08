#Crie uma tupla preenchida com os 20 primeiros colocados do campeonato brasileiro de futebol, na ordem da colocação.
#depois mostre:
#A) Apenas os 5 primeiros colocados.
#B) Os últimos 4 colocados da tabela.
#C) Uma lista com os times em ordem alfabética.
#D) Em que posição na tabela está o time da chapecoense.

import unicodedata

tupla_brasileirao = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo', 'Bahia', 'São Paulo', 'Grêmio', 'Red Bull Bragantino', 'Atlético Mineiro', 'Santos', 'Corinthians', 'Vasco', 'Vitória', 'Internacional', 'Ceará', 'Fortaleza', 'Juventude', 'Recife')
brasileirao_ordenado = sorted(tupla_brasileirao)

print('-=' * 30)
print(f'Lista de times do Brasileirão: {tupla_brasileirao}')
print('-=' * 30)
print(f'Os cinco primeiros são: {tupla_brasileirao[:5]}')
print('-=' * 30)
print(f'Os quatro últimos são: {tupla_brasileirao[-4:]}')
print('-=' * 30)
print(f'Times na ordem alfabética: {sorted(tupla_brasileirao)}')
print('-=' * 30)
print(f'O Atlético Mineiro está na {tupla_brasileirao.index("Atlético Mineiro") + 1}° posição')


def normalizar(texto):
    return unicodedata.normalize('NFD', texto)\
        .encode('ascii', 'ignore')\
        .decode()\
        .title()

while True:
    print(f'{"Brasileirão":=^50}')
    print('1 - Cinco primeiros colocados da tabela'
          '\n2 - Quatro últimos colocados da tabela'
          '\n3 - Lista com todos os times do brasileirão em ordem alfabética'
          '\n4 - Posição de algum time especifico'
          '\n5 - Tabela completa do Brasileirão'
          '\n0 - Sair')

    opcao = int(input('O que deseja ver? '))

    if opcao == 1:
        print(f'\033[30;42mOs 5 primeiros colocados sâo:\033[m')
        for i in range(5):
            print(f'\033[92m{i + 1}° - {tupla_brasileirao[i]}\033[m')

    elif opcao == 2:
        print('\033[30;41mOs últimos 4 colocados da tabela são:\033[m')
        for i in range(16, 20):
            print(f'\033[91m{i+1} - {tupla_brasileirao[i]}\033[m')

    elif opcao == 3:
        print('\033[30;46mA lista com os times do brasileirão em ordem alfabética é:\033[m')
        for time in brasileirao_ordenado:
            print(f'\033[36m{time}\033[m')

    elif opcao == 4:
        tupla_sem_assento = tuple(normalizar(time1) for time1 in tupla_brasileirao)
        time = normalizar(input('informe o nome do time que deseja ver a posição: '))

        if time in tupla_sem_assento:
            print(f'\033[30;43mO {tupla_brasileirao[tupla_sem_assento.index(time)]} está na {tupla_sem_assento.index(time) + 1}° posição.\033[m')

    elif opcao == 5:
        print('\033[30;44mTabela completa do brasileirão série A\033[m')
        for posicao, time in enumerate(tupla_brasileirao):
            print(f'\033[34m{posicao + 1:<2} - {time}\033[m')

    else:
        break

