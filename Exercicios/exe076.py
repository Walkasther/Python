#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tupla_preço = 'Arroz',13.99, 'Feijão', 6.99, 'Açai', 5, 'Poupa', 2.5, 'Carne de sol',19.99

print(f'{'-'*50}\n{'Supermercado Guanabara':^50}\n{'-'* 50}')
for c,produto in enumerate(tupla_preço):
    if c % 2 == 0: print(f'{produto:.<40}',end='')
    else: print(f'R$  {produto:.2f}')
