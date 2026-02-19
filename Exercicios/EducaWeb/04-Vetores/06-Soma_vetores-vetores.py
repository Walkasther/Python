# Faça um programa para ler dois vetores A e B, contendo N elementos cada. Em seguida, gere um
# terceiro vetor C onde cada elemento de C é a soma dos elementos correspondentes de A e B. Imprima
# o vetor C gerado.

n = int(input('Quantos valores vai ter cada vetor? '))

a = []
b = []
c = []

print('Digite os valores do vetor A:')
for _ in range(n):
    a.append(int(input()))

print('Digite os valores do vetor B:')
for _ in range(n):
    b.append(int(input()))

print('VETOR RESULTANTE:')
for i in range(n):
    c.append(a[i] + b[i])
    print(c[i])