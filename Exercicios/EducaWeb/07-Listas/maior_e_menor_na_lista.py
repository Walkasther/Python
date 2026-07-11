valores = []

for i in range(5):
    valores.append(int(input(f'Digite o {i + 1}° valor: ')))

maior = max(valores)
menor = min(valores)

print(f'Valores Digitados: {valores}')

print(f'O maior valor da lista é {maior}', 'na posição' if valores.count(maior) == 1 else 'nas posições', end =' ')
for posicao, valor in enumerate(valores):
    if valor == maior:
        print(posicao, end=' ')

print(f'\nO menor valor da lista é {menor}', 'na posição' if valores.count(menor) == 1 else 'nas posições', end=' ')
for posicao, valor in enumerate(valores):
    if valor == menor:
        print(posicao, end=' ')

