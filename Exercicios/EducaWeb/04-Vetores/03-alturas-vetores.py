# Fazer um programa para ler nome, idade e altura de N pessoas, conforme exemplo. Depois, mostrar na
# tela a altura média das pessoas, e mostrar também a porcentagem de pessoas com menos de 16 anos,
# bem como os nomes dessas pessoas caso houver.
from itertools import count

n = (int(input('Quantas pessoas serao digitadas: ')))

total_menor = 0
nome = []
idade = []
altura = []

for i in range(n):
    print(f'Dados da {i+1}° Pessoa:')
    nome.append(input('Nome: '))
    idade.append(int(input('Idade: ')))
    altura.append((float(input('Altura: '))))

    if idade[i] < 16:
        total_menor += 1

media_altura = sum(altura) / len(altura)
print(f'Altura media: {media_altura}')

print('porcentagem das pessoas com menos de 16 anos: ')

menor_16 = total_menor / n * 100
print(f'{menor_16:.1f}%', end=' ')
for i in range(n):
    if idade[i] < 16:
        print(nome[i])


#nome das pessoas com menos de 16