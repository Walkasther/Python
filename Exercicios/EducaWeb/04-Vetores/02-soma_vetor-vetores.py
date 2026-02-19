# Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida:
# - Imprimir todos os elementos do vetor
# - Mostrar na tela a soma e a média dos elementos do vetor.

n = int(input('Quantos numeros voce vai digitar? '))
valores = []

for _ in range(n):
    valores.append(float(input('Digite um numero: ')))

print(f'VALORES =', end=' ')
for valor in valores:
    print(f'{valor:.1f}', end=' ')
print()

soma = sum(valores)
media = soma / len(valores)

print(f'SOMA = {soma:.2f}')
print(f'MEDIA = {media:.2f}')
