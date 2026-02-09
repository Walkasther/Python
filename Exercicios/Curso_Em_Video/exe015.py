# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o
# carro custa R$60 por dia e R$0,15 por Km rodado.


dias = int(input('Por quantos dias ele foi alugado? '))
km_percorrido = float(input('Quantos km percorridos? '))
preco_aluguel = 60
preco_gasolina = 0.15

valor_a_pagar = (preco_aluguel * dias) + (km_percorrido * preco_gasolina)

print('\033[1;30;107mValor a pagar: R${:.2f}'.format(valor_a_pagar))
