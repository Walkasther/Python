# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que
# Ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
print('\033[31m')
nome1 = input('Anulo 1: ')
nome2 = input('Aluno 2: ')
nome3 = input('Aluno 3: ')
nome4 = input('Aluno 4: ')
nomes = [nome1, nome2, nome3, nome4]
sorteado = choice(nomes)

print('\033[91mO aluno sorteado foi o {}'.format(sorteado))