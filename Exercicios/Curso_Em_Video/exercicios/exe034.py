#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
#Para salários inferiores ou iguais, o aumento é de 15%.

s = int(input('\033[45;97mQual o seu salário atual? R$'))
n = ...
if s > 1250:
    n = s + s * 0.1
else:
    n = s + s * 15 / 100
print('\033[41;93mO seu novo salário é R$ {:.2f}\033[m'.format(n))
