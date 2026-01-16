n = int(input("Quantos elementos vai ter o vetor? "))
vet = [0 for i in range (n)]
mediaPar = 0
c = 0
for i in range (0,n):
    vet[i] = int(input("Digite um numero: "))

for i in range (0,n) :
    if vet[i] % 2 == 0 :
        c = c +1
        mediaPar = mediaPar + vet[i]

if mediaPar != 0:
    mediaPar = mediaPar / c
    print(f"MEDIA DOS PARES = {mediaPar:.1f}")
else:
    print("NENHUM NUMERO PAR")