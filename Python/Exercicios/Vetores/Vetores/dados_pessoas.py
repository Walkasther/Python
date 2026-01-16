n = int(input("Quantas pessoas serao digitadas? "))
altura = [0 for i in range(n)]
genero = [0 for i in range(n)]

for i in range (0,n):
    altura[i] = float(input(f"Altura da {i+1}° pessoa: "))
    genero[i] = input(f"Gênero da {i+1}° pessoa: ")

maior = altura[0]
menor = altura[0]
media_mulheres = 0
numero_homens = 0
c = 0

for i in range (0,n):
    if altura[i] > maior:
        maior = altura[i]
    elif altura[i] < menor:
        menor = altura[i]

    if genero[i] == "f" or genero[i] == "F":
        media_mulheres = media_mulheres + altura[i]
        c = c + 1
    else:
        numero_homens = numero_homens + 1

media_mulheres = media_mulheres / c
print(f"Menor altura = {menor:.2f}")
print(f"Maior altura = {maior:.2f}")
print(f"Media das alturas das mulheres = {media_mulheres:.2f}")
print(f"Numero de homens = {numero_homens}")