n = int(input("Quantos alunos serão digitados? "))
nome = [0 for i in range (n)]
n1 = [0 for i in range(n)]
n2 = [0 for i in range(n)]

for i in range(0,n):
    print(f"Digite nome, primeira e segunda nota do {i+1}° aluno:")
    nome[i] = input()
    n1[i] = float(input())
    n2[i] = float(input())

print("Alunos aprovados: ")
for i in range (0,n):
    if (n1[i] + n2[i]) / 2 >= 6:
        print(nome[i])