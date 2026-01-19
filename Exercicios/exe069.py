#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
#A) Quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

print(f'{'Cadastrador de pessoas':-^50}')
c = 1
mais_18 = 0
homem = 0
mulher_menor = 0
while True:
    idade = int(input(f'Digite a idade da {c}° pessoa: '))
    sexo = input(f'Informe o sexo da {c} pessoa. [M]Masculino [F]Feminino: ')
    continuar = int(input('Quer continuar? [0]SIM [1]NÃO: '))
    if idade > 18:
        mais_18 += 1
    if sexo in ['m','M']:
        homem += 1
    if sexo in ['f','F'] and idade < 20:
        mulher_menor += 1
    if continuar == 0:
        c += 1
    else:
        break

print(f'\033[33mPessoas com mais de 18 anos: {mais_18}')
print(f'\033[32mQuantidade de homens cadastrados: {homem}')
print(f'\033[31mQuantidade de mulheres com menos de 20 anos: {mulher_menor}')