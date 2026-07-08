produtos = ('Arroz', 14.99, 'Feijão', 6.99, 'Macarrão', 3.99, 'carne', 10.90, 'iogurte', 8.99, 'achocolatado', 1.99, 'Sabonete', 0.99, 'Shampoo', 6.99, 'Condicionador', 8.99, 'biscoito', 2.99)
c1 = 0
c2 = 1

print('-' * 35)
print(f'{'LISTAGEM DE PREÇOS':^35}')
print('-' * 35)
for produto in produtos:
    if produtos.index(produto) % 2 == 0:
        print(f'{produto:.<30}', end='')
    else:
        print(f'R${produto:>6}')
print('-' * 35)