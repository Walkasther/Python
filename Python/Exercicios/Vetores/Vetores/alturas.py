n = int(input("Quantas pessoas serão digitadas? "))
nome = [0 for i in range (n)]
idade = [0 for i in range (n)]
altura = [0 for i in range (n)]

for i in range (0,n):
    print(f"Dados da {i+1}° pessoa:")
    nome[i] = input("Nome: ")
    idade[i] = int(input("Idade: "))
    altura[i] = float(input("Altura: "))

media_altura = 0
menos16 = 0
for i in range (0,n):
    media_altura = media_altura + altura[i]
    if idade[i] < 16 :
        menos16 = menos16 + 1

media_altura = media_altura / n
pmenos16 = menos16 / n * 100

print(f"\nAltura média: {media_altura:.2f}")
print(f"Pessoas com menos de 16 anos: {pmenos16}%")
for i in range (0,n) :
    if idade[i] < 16 :
        print(nome[i])