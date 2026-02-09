#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de
#cada aluno individualmente.
sala = []
pos = 0
while True:
    nome = []
    nota = []
    nome.append(input('Nome: '))
    nota.append((float(input('Nota 1: '))))
    nota.append(float(input('Nota 2: ')))
    sala.append(nome)
    sala[pos].append(nota)
    continuar = input('Quer continuar? [S]SIM [N]NÃO: ').strip().upper()[0]
    if continuar == 'N':
        break
    pos += 1
print('-' * 30)
print(f'N°{'Nome':^20}Média')
print('-' * 30)
for i, c in enumerate(sala):
    media = (sala[i][1][0] + sala[i][1][1]) / 2
    print(f'{i}{sala[i][0]:^20}{media}')

while True:
    print('-' * 30)
    mostrar_notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar_notas == 999:
        break
    print(f'As notas de {sala[mostrar_notas][0]} são {sala[mostrar_notas][1]}')