#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#-A vista dinheiro/cheque: 10% de desconto
#-A vista no cartão: 5% de desconto
#-Em até 2x no cartão: preço normal
#-3x ou mais no cartão: 20% de juros

print(f'{' LOJAS GUANABARA ':=^40}')
preco = float(input('Digite o preço normal do produto: R$'))
novo_preco = None
pagamento = input('\n\033[32m[1]-A vista (dinheiro/cheque)'
                  '\n\033[33m[2]-A vista no cartão'
                  '\n\033[34m[3]-Em 2x no cartão'
                  '\n\033[35m[4]- em 3x ou mais no cartão'
                  '\n\n\033[97mInforme a forma de pagamento:')
if pagamento == '1':
    novo_preco = preco - preco * 10 / 100
    print('O valor do produto a vista no dinheiro ou cheque vai ficar R${:.2f}'.format(novo_preco))
elif pagamento == '2':
    novo_preco = preco - preco * 5 / 100
    print(f'O valor do produto a vista no cartão vai ficar R${novo_preco:.2f}')
elif pagamento == '3':
    print(f'O valor do produto vai ficar R${preco:.2f} em 2x de R${preco /2:.2f} sem juros no cartão.')
elif pagamento == '4':
    n_parcelas = int(input('Quantas parcelas? '))
    novo_preco = preco + preco * 20 / 100
    v_parcelas = novo_preco / n_parcelas
    print(f'O valor do produto vai ficar R${novo_preco:.2f} em {n_parcelas}x de R${v_parcelas:.2f} no cartão.')
else:
    print('\033[31mEscolha uma opção válida!')
