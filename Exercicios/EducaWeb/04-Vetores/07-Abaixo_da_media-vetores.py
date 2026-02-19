# Fazer um programa para ler um número inteiro N e depois um vetor de N números reais. Em seguida,
# mostrar na tela a média aritmética de todos os elementos com três casas decimais. Depois mostrar todos
# os elementos do vetor que estejam abaixo da média, com uma casa decimal cada.

n = int(input('Quantos elementos vai ter o vetor? '))
valores = []

for _ in range(n):
    valores.append(float(input('Digite um número: ')))

media = sum(valores) / len(valores)

print(f'MEDIA DO VETOR = {media:.3f}')
print('ELEMENTOS ABAIXO DA MEDIA: ')

for valor in valores:
    if valor < media:
        print(f'{valor:.1f}')