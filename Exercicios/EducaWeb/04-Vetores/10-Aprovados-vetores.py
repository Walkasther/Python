# Fazer um programa para ler um conjunto de N nomes de alunos, bem como as notas que eles tiraram
# no 1º e 2º semestres. Cada uma dessas informações deve ser armazenada em um vetor. Depois, imprimir
# os nomes dos alunos aprovados, considerando aprovado aqueles cuja média das notas seja maior ou
# igual a 6.0 (seis).

n = int(input('Quantos alunos serao digitados? '))

nomes = []
notas_1 = []
notas_2 = []

for i in range(n):
    print(f'Digite nome, primeira e segunda nota do {i + 1}° aluno: ')
    nomes.append(input())
    notas_1.append(float(input()))
    notas_2.append(float(input()))

print('Alunos aprovados:')

for i in range(n):
    media = (notas_1[i] + notas_2[i]) / 2

    if media >= 6:
        print(nomes[i])