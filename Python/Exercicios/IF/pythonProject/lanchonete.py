cod = int(input("Codigo do produto comprado: "))
quantidade = int(input("Quantidade comprada: "))
valor : float
total : float

if cod == 1 :
    valor = 5.00
elif cod == 2:
    valor = 3.50
elif cod == 3:
    valor = 4.80
elif cod == 4:
    valor = 8.90
elif cod == 5:
    valor = 7.32
else:
    valor = "Código invalido!"

total = valor * quantidade
print(f"Valor a pagar: R$ {total:.2f}")