n = int(input("Quantas pessoas voce vai digitar? "))
vet_nome = [0 for i in range (n)]
vet_idade = [0 for i in range (n)]
maior = 0
for i in range (0,n):
    print(f"Dados da {i+1}°  pessoa: ")
    vet_nome[i] = input("Nome: ")
    vet_idade[i] = int(input("Idade: "))

for i in range (0,n):
    if vet_idade[i] > vet_idade[i-1]:
        maior = i

print("PESSOA MAIS VELHA: ",vet_nome[maior])