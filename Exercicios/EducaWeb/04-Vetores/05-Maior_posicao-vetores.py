# Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida, mostrar na tela
# o maior número do vetor (supor não haver empates). Mostrar também a posição do maior elemento,
# considerando a primeira posição como 0 (zero).

n = int(input('Quantos numeros voce vai digitar: '))
vetor_1 = []

for _ in range(n):
    vetor_1.append(float(input('Digite um numero: ')))

print(f'MAIOR VALOR: {max(vetor_1)}')
print(f'POSICAO DO MAIOR VALOR: {vetor_1.index(max(vetor_1))}')
