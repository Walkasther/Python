#Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia. O programa deve ler
# o preço unitário do produto, a quantidade unidades compradas deste produto, e o valor em dinheiro dado pelo cliente
# (Suponha que haja dinheiro suficiente). Seu programa deve mostrar o valor do troco a ser devolvido ao cliente.

preco_produto = float(input('Preço unitário do produto: R$'))
quantidade_comprada = int(input('Quantidade comprada: '))
dinheiro_recebido = float(input('Dinheiro recebido: R$'))

total = preco_produto * quantidade_comprada
troco = dinheiro_recebido - (preco_produto * quantidade_comprada)

print(f'TROCO: R$ {troco:.2f}')
