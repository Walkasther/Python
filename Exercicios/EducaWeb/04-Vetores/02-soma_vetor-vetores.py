# Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida:
# - Imprimir todos os elementos do vetor
# - Mostrar na tela a soma e a média dos elementos do vetor.

n = int(input('Quantos numeros voce vai digitar? '))
vetor_1 = []

for _ in range(n):
    vetor_1.append(float(input('Digite um numero: ')))

print(f'VALORES = {vetor_1}')
print(f'SOMA = {sum(vetor_1):.2f}')
print(f'MEDIA = `{sum(vetor_1) / len(vetor_1):.2f}')