# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('{}A média desse aluno foi: {:.1f}'.format('\033[92m' if m >= 7 else '\033[91m',m))