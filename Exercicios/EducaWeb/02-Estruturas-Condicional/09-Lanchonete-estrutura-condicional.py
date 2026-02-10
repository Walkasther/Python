# Uma lanchonete possui vários produtos. Cada produto possui um código e um preço. Você deve fazer um programa para
# ler o código e a quantidade comprada de um produto (suponha um código válido), e daí informar qual o valor a ser
# pago, com duas casas decimais, conforme tabela abaixo:
#Código do produto | Preço do produto
# 1   |   R$ 5.00
# 2   |   R$ 3.50
# 3   |   R$ 4.80
# 4   |   R$ 8.90
# 5   |   R$ 7.32

codigo_produto = int(input('Código do produto comprado: '))
quantidade = int(input('Quantidade comprada: '))

if codigo_produto == 1:
    preco_final = quantidade * 5

elif codigo_produto == 2:
    preco_final = quantidade * 3.50

elif codigo_produto == 3:
    preco_final = quantidade * 4.80

elif codigo_produto == 4:
    preco_final = quantidade * 8.90

elif codigo_produto == 5:
    preco_final = quantidade * 7.32

print(f'Valor a pagar: R$ {preco_final:.2f}')