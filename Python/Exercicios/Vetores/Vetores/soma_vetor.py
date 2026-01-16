n = int(input("Quantos números voce vai digitar? "))
vet = [0 for i in range(n)]

for i in range(0,n):
    vet[i] = float(input("Digite um numero: "))

soma = 0
print("VALORES = ", end="")
for i in range (0,n):
    print(f"{vet[i]:.1f}", end=" ")
    soma = soma + vet[i]

media = soma / n
print(f"\nSOMA = {soma:.2f}")
print(f"MÉDIA = {media:.2f}")