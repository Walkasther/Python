n = int (input("Serão digitados dados de quantos produtos? "))
produto = [0 for i in range(n)]
preco_compra = [0 for i in range (n)]
preco_venda = [0 for i in range (n)]

for i in range (0,n):
    print(f"Produto {i+1}:")
    produto[i] = input("Nome: ")
    preco_compra[i] = float(input("Preco de compra: "))
    preco_venda[i] = float(input("Preco de venda: "))

menor_de_10 = 0
menor_de_20 = 0
maior_de_20 = 0
total_compra = 0.00
total_venda = 0.00

for i in range(0,n):
    p = (preco_venda[i] - preco_compra[i]) / preco_compra[i] * 100
    total_compra = total_compra + preco_compra[i]
    total_venda = total_venda + preco_venda[i]
    if p < 10 :
        menor_de_10 = menor_de_10 + 1
    elif 10 <= p <= 20:
        menor_de_20 = menor_de_20 + 1
    else:
        maior_de_20 = maior_de_20 + 1

lucro_total = total_compra - total_venda

print("\nRELATORIO:")
print(f"Lucro abaixo de 10%: {menor_de_10}")
print(f"Lucro entre 10% e 20%: {menor_de_20}")
print(f"Lucro acima de 20%: {maior_de_20}")
print(f"Valor total de compra: {total_compra:.2f}")
print(f"Valor total de venda: {total_venda}")
print(f"Lucro total: {lucro_total}")