n = int(input("Quantos números voce vai digitar? "))
vet = [0 for i in range (n)]

for i in range (0,n):
    vet[i] = int(input("Digite um numero: "))

c = 0

for i in range (0,n):
    if vet[i] % 2 == 0:
        print(vet[i], end=" ")
        c = c + 1

print(f"\nQuantidade de pares: {c}")