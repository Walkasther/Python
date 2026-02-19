# Fazer um programa para ler um conjunto de nomes de pessoas e suas respectivas idades. Os nomes
# devem ser armazenados em um vetor, e as idades em um outro vetor. Depois, mostrar na tela o nome
# da pessoa mais velha.

n = int(input('Quantas pessoas voce vai digitar? '))

nomes = []
idades = []

for i in range(n):
    print(f'Dados da {i + 1}a pessoa:')
    nomes.append(input('Nome: '))
    idades.append(int(input('Idade: ')))

print(f'PESSOA MAIS VELHA: {nomes[idades.index(max(idades))]}')