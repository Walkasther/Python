# Tem-se um conjunto de dados contendo a altura e o gênero (M, F) de N pessoas. Fazer um programa
# que calcule e escreva a maior e a menor altura do grupo, a média de altura das mulheres, e o número
# de homens.

n = int(input('Quantas pessoas serao digitadas? '))

alturas = []
sexos = []
soma_altura_mulheres = quantidade_mulheres = quantidade_homens = 0

for i in range(n):
    alturas.append(float(input(f'Altura da {i + 1}a pessoa: ')))
    sexos.append(input(f'Sexo da {i+1}a pessoa: ').upper())

    if sexos[i] == 'F':
        soma_altura_mulheres += alturas[i]
        quantidade_mulheres += 1
    else:
        quantidade_homens += 1


media_altura_mulheres = soma_altura_mulheres / quantidade_mulheres if quantidade_mulheres > 0 else 0

print(f'Menor altura = {min(alturas):.2f}')
print(f'Maior altura = {max(alturas):.2f}')
print(f'Media das alturas das mulheres = {media_altura_mulheres:.2f}')
print(f'Numero de homens = {quantidade_homens}')
