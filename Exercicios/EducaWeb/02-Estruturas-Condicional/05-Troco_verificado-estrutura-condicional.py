# Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
# O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
# e o valor em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do troco a ser devolvido
# ao cliente. Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem informando o
# valor restante.

preco = float(input('Preço unitário do produto: '))
quantidade = int(input('Quantidade comprada: '))
dinheiro_recebido = float(input('Dinheiro Recebido: '))

valor_a_pagar = preco * quantidade


if valor_a_pagar > dinheiro_recebido:
    faltante = valor_a_pagar - dinheiro_recebido
    print(f'DINHEIRO INSUFICIENTE. FALTAM {faltante:.2f} REAIS ')
else:
    troco = dinheiro_recebido - valor_a_pagar
    print(f'TROCO = {troco:.2f}')