produtos = ('Arroz', 14.99, 'Feijão', 6.99, 'Macarrão', 3.99, 'carne', 10.90, 'iogurte', 8.99, 'achocolatado', 1.99, 'Sabonete', 0.99, 'Shampoo', 6.99, 'Condicionador', 8.99, 'biscoito', 2.99)

print('-' * 35)
print(f'{'LISTAGEM DE PREÇOS':^35}')
print('-' * 35)
#Solução 1:
for produto in produtos:
    if produtos.index(produto) % 2 == 0:
        print(f'{produto:.<30}', end='')
    else:
        print(f'R${produto:>6.2f}')
print('-' * 35)

#Solução 2:
for produto in produtos:
    print(f'{produto:.<30}' if produtos.index(produto) % 2 == 0 else f'R${produto:>6.2f}\n', end='')
print('-' * 35)
#Solução 3:
for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:.<30} R${produtos[i+1]:>6.2f}')
print('-' * 35)