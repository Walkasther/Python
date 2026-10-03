# Crie um programa que leia nome, sexo, e idade de várias pessoas, guardando os dados de cada
# pessoa em um dicionário, e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.

from Curso_Em_Video.Aulas.cores import cores_claras2

pessoas = []

while True:
    pessoa = dict(nome = input('Nome: '))

    while True:
        pessoa['sexo'] = input('Sexo: ').strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))

    pessoas.append(pessoa)

    while True:
        continuar = input('\033[44;30mQuer continuar? [S]im | [N]ão:\033[m ').strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')

    if continuar == 'N':
        break

idade_media = sum(pessoa['idade'] for pessoa in pessoas) / len(pessoas)
mulheres = [pessoa["nome"] for pessoa in pessoas if pessoa["sexo"] == 'F']

print(f'{cores_claras2["amarelo_claro"]}- O grupo tem {len(pessoas)} pessoas.')
print(f'{cores_claras2["azul_claro"]}- A média de idade do grupo é de: {idade_media:.2f} anos.')
print(f'{cores_claras2["verde_claro"]}- Mulheres do grupo: {mulheres}')

print(f'{cores_claras2["vermelho_claro"]}Lista de pessoas que estão acima da média:')
for pessoa in pessoas:
    if pessoa['idade'] > idade_media:
        for k,v in pessoa.items():
            print(f'{k} = {v};', end=' ')
        print()

print('<<ENCERRADO>>')