 #Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
 #a ser sacado(número inteiro), e o programa vai informar quantas cédulas de cada valor serão entregues.
 #OBS: Considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1.

print('=' * 50)
print(f'{'BANCO DIGITAL':-^50}')
print('=' * 50)
#nota_50 = nota_20 = nota_10 = nota_1 = 0
valor = int(input('Qual valor você quer sacar? R$'))
valor2 = valor
nota_50 = valor2 // 50
valor2 -= nota_50 * 50
nota_20 = valor2 // 20
valor2 -= nota_20 * 20
nota_10 = valor2 // 10
valor2 -= nota_10 * 10
nota_1 = valor2 // 1
print(f'Total de:')
if nota_50 > 0:
      print(f'\033[31m{nota_50} Cédulas de R$50')
if nota_20 > 0:
      print(f'\033[32m{nota_20} Cédulas de R$20')
if nota_10 > 0:
      print(f'\033[33m{nota_10} Cédulas de R$10')
if nota_1 > 0:
      print(f'\033[34m{nota_1} Cédulas de R$1')

print('\033[97m=' * 50)
print('\033[35mVolte sempre ao banco digital! \nTenha um bom dia!')