n = int(input("Quantos números voce vai digitar? "))
d = 0
f = 0

for i in range (0,n) :
    x = int(input("Digite um numero: "))
    if 10 <= x >= 20 :
        d = d + 1
    else:
        f = f  + 1

print(d," DENTRO")
print(f," FORA")