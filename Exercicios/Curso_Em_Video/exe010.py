# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

dolar = 3.27
real = float(input('Quantos reais você rem na carteira? R$ '))
conversor = real / dolar
print('\033[7;4;32mCom esse valor, você consegue comprar {:.2f} Dólar(es)'.format(conversor))
