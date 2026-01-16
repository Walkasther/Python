n = int(input("Quantos elementos vai ter o vetor?  "))
vet = [0 for i in range (n)]
media = 0

for i in range (0,n):
    vet[i] = float(input("Digite um numero: "))

for i in range (0,n):
    media = media + vet[i]

media = media / n
print(f"\nMÉDIA DO VETOR: {media:.3f}")
print("Elementos abaixo da média:")
for i in range (0,n):
    if vet[i] < media :
        print(f"{vet[i]:.1f}")