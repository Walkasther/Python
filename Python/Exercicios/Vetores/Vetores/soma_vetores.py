n = int(input("Quantos valores vai ter cada vetor? "))
a = [0 for i in range (n)]
b = [0 for i in range (n)]
c = [0 for i in range (n)]

print("Digite os valores do vetor A")
for i in range (0,n):
    a[i] = int(input())

print("Digite os valores do vetor B")
for i in range (0,n):
    b[i] = int(input())

for i in range(0,n):
    c[i] = a[i] + b[i]

print("VETOR RESULTANTE:")
for i in range (0,n):
    print(c[i])