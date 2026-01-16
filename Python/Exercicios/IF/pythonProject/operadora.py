plano = 50.00
minuto = 2.00
tempo = int(input("Digite a quantidade de minutos: "))

if tempo > 100:
    preco = plano + ((tempo - 100) * 2)
else:
    preco = plano

print(f"Valor a pagar: R$ {preco:.2f}")