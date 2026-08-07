#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre
#o conteúdo da estrutura na tela.

nome = input('Insira o nome do Anulo: ')
media = float(input('insira a media do aluno: '))

aluno = {'nome':nome,
         'media':media,
         'situacao':'\033[32mAPROVADO' if media >= 7 else '\033[33mRECUPERAÇÃO' if media >= 5 else '\033[31mREPROVADO' }

print(f'Nome do aluno: {aluno["nome"]}')
print(f'Média do aluno: {aluno["media"]}')
print(f'Situação do aluno: {aluno["situacao"]}')

#---------------------------------------------------------------
#Solução 2

aluno2 = {'Nome':input('Insira o nome do Anulo: '),
         'Media':float(input('insira a media do aluno: '))}
if aluno2['Media'] >= 7:
    aluno2['Situacao'] = 'Aprovado'
elif aluno2['Media'] >= 5:
    aluno2['Situacao'] = 'Recuperação'
else:
    aluno2['Situacao'] = 'Reprovado'

for k, v in aluno2.items():
    print(f'{k} do aluno: {v}')
