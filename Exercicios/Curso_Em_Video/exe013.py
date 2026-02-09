# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o salário atual do funcionário? R$'))
print('\033[92mO novo salário do funcionário é R${:.2f}'.format(salario + salario * 15 / 100))