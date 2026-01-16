print("Digite as tres distancias:")
a = float(input())
b = float(input())
c = float(input())

if a > b and a > c :
    maior = a
elif b > c :
    maior = b
else:
    maior = c

print(f"MAIOR DISTANCIA = {maior:.2f}")