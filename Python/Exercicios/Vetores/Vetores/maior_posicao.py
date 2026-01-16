n = int(input("quantos números você vai digitar? "))
vet = [ 0 for i in range (n)]
c = 0
p = 0
for i in range (0,n):
    vet[i] = float(input("Digite um numero: "))
    if c < vet[i]:
        c = vet[i]
        p = i

print(f"\nMAIOR VALOR = {c:.2f}")
print("POSIÇÃO DO MAIOR VALOR = ", p)