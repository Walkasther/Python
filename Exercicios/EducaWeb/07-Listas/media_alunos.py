alunos = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados = [nome, [nota1, nota2], media]
    alunos.append(dados[:])

    continuar = input('Quer continuar? [S]im [N]ão: ').strip().upper()

    if continuar == 'N':
        break

print(alunos)
print('-=' * 15)

print('N°    NOME      MÉDIA')
print('-' * 25)
for i,aluno in enumerate(alunos):
    print(f'{i:<6}{aluno[0]:<10}{aluno[2]:.1f}')

print('-' * 25)

while True:
    mostrar_notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if mostrar_notas == 999:
        break

    print(f'Notas de {alunos[mostrar_notas][0]} São {alunos[mostrar_notas][1]}')
    print('-' * 25)

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
