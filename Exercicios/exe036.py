#Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o sálario do comprador e em quantos anos ele vai pagar.
#Calcule  o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, ou então
#o empréstimo será negado.

v_casa = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Quanto você ganha por mês? R$'))
anos = int(input('em quantos anos pretende pagar a casa? '))

prestacao = v_casa / (12 * anos)

if prestacao <= salario * 0.3:
    print(f'Empréstimo concedido! o valor qda prestação será de R${prestacao:.2f}')
else:
    print('Empréstimo negado, o valor da prestação R${:.2f} excede 30% do salário'.format(prestacao))
