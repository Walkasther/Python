n = int (input("Quantos números voce vai digitar? "))
vet = [ 0 for i in range (n)]

for i in range(0,n):
    vet[i] = int(input("Digite um numero: "))

print("\nNÚMEROS NEGATIVOS:")

for i in range (0,n):
    if vet[i] < 0:
        print(vet[i])