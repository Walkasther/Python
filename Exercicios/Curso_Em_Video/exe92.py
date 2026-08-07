#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
#Se por acaso a ctps for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e
#acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
from random import choice
from Curso_Em_Video.Aulas.cores import cores_claras

ano_atual = datetime.now().year

pessoa = dict(nome = input('Nome: '),
              idade = ano_atual - int(input('Ano de nascimento: ')),
              ctps = int(input('Carteira de trabalho: '))
              )

if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['aposentadoria'] = ((pessoa['contratacao'] + 35) - ano_atual) + pessoa['idade']

print('-='*30)
for i,(k, v) in enumerate(pessoa.items()):
    print(f'{cores_claras[i % len(cores_claras)]}{k} tem valor {v}')