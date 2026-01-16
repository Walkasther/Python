a = int(input("Hora inicial: "))
b = int(input("Hora Final: "))

if a >= b :
    c = 24 - a + b
else:
    c = b - a

print(f"O JOGO DUROU {c} HORA(S) ")