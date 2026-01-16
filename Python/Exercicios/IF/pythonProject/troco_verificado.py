preco = float(input("Preço unitário do produto: "))
quantidade = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinheiro recebido: "))

if dinheiro > preco * quantidade:
    troco = dinheiro - (preco * quantidade)
    print(f"TROCO = {troco:.2f}")
else:
    troco = preco * quantidade - dinheiro
    print(f"DINHEIRO INSUFICIENTE. FALTAM {troco:.2f} REAIS")