#Crie uma tupla preenchida com os 20 primeiros colocados do campeonato brasileiro de futebol, na ordem da colocação.
#depois mostre:
#A) Apenas os 5 primeiros colocados.
#B) Os últimos 4 colocados da tabela.
#C) Uma lista com os times em ordem alfabética.
#D) Em que posição na tabela está o time da chapecoense.

tupla_brasileirao = 'Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo', 'Bahia', 'São Paulo', 'Grêmio', 'Red Bull Bragantino', 'Atlético Mineiro', 'Santos', 'Corinthians', 'Vasco', 'Vitória', 'Internacional', 'Ceará', 'Fortaleza', 'Juventude', 'Recife'

print(f'\033[32m{'-=' * 30}\nOs cinco primeiros colocados são:')
for c,time in enumerate(tupla_brasileirao[0:5]):
    print(f'{c+1}- {time}')

print(f'\033[31m{'-=' * 30}\nOs quatro últimos colocados no tabela são:')
for c,time in enumerate(tupla_brasileirao[-4:]):
    print(f'{len(tupla_brasileirao) - 3 + c}- {time}')

print(f'\033[33m{'-=' * 30}\nTimes em ordem alfabética: ')
print(sorted(tupla_brasileirao))

print(f'\033[34m{'-=' * 30}\nO Corinthians está na {tupla_brasileirao.index('Corinthians') + 1}° posição.')