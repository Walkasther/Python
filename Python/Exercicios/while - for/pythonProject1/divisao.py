n = int(input("Quantos casos voce vai digitar? "))

for i in range(0,n):
    x = int(input("Entre com o numerador: "))
    y = int(input("Entre com o denominador: "))
    if y == 0:
        print("DIVISÃO IMPOSSÍVEL ")
    else:
        print(f"DIVISÃO: {x/y:.2f}")