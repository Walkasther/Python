# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import  sample, shuffle
print('\033[32m')
nomes = [input('Aluno 1: '), input('Aluno 2: '), input('Aluno 3: '), input('Aluno 4: ')]

#solução 1
shuffle(nomes)
print('\033[92mA ordem da apresentação será: {}'.format(nomes))

#Sloução 2
ordem = sample(nomes, k= 4)
print('A ordem da apresentação será: {}'.format(ordem))
