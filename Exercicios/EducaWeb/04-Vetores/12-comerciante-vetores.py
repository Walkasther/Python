# Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele comercializa. Para isto,
# mandou digitar um conjunto de N mercadorias, cada uma contendo nome, preço de compra e preço de
# venda das mesmas. Fazer um programa que leia tais dados e determine e escreva quantas mercadorias
# proporcionaram:
#  lucro < 10%
#  10% ≤ lucro ≤ 20%
#  lucro > 20%
# Determine e escreva também o valor total de compra e de venda de todas as mercadorias, assim como
# o lucro total.

n = int(input('Serao digitados dados de quantos produtos? '))

nomes = []
precos_compra = []
precos_venda = []

lucro_baixo = lucro_medio = lucro_alto = 0

for i in range(n):
    print(f'Produto {i+1}')
    nomes.append(input('Nome: '))
    precos_compra.append(float(input('Preco de compra: ')))
    precos_venda.append(float(input('Preco de venda: ')))

    lucro = precos_venda[i] - precos_compra[i]
    porcentagem = lucro / precos_compra[i] * 100

    if porcentagem < 10:
        lucro_baixo += 1
    elif 10 <= porcentagem <= 20:
        lucro_medio += 1
    else:
        lucro_alto += 1

total_compra = sum(precos_compra)
total_venda = sum(precos_venda)
lucro_total = total_venda - total_compra

print('RELATORIO:')
print(f'Lucro abaixo de 10%: {lucro_baixo}')
print(f'Lucro entre 10% e 20%: {lucro_medio}')
print(f'Lucro acima de 20%: {lucro_alto}')
print(f'Valor total de compra: {total_compra:.2f}')
print(f'Valor total de venda: {total_venda:.2f}')
print(f'Lucro total: {lucro_total:.2f}')