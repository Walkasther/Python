# Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a
# média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao
# intervalo [0,10]). Cada nota deve ser validada separadamente.

nota_1 = float(input('Digite a primeira nota: '))

while nota_1 < 0 or nota_1 > 10:
    nota_1 = float(input('Valor invalido! Tente novamente: '))

nota_2 = float(input('Digite a segunda nota: '))

while nota_2 < 0 or nota_2 > 10:
    nota_2 = float(input('Valor invalido! Tente novamente: '))

media = (nota_1 + nota_2) / 2

print(f'MÉDIA = {media:.2f}')
