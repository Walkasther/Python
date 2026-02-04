a = [1,2,3,4,5,6,7,8]
b = a.copy()
b.append(15)
b[5] = 10
#a.clear()
print(f'A = {a}')
print(f'B = {b}')
n = [int(input('Digite um número:')) for x in range(5)] # Já inicia a lista com a quantidade de espaços determinada, nesse caso 5. Pode ser aumentado ou diminuído depois.
print(f'N: {n}')



lanche = ['Pão', 'Suco', 'Pizza', 'Salgado']
print(lanche)
lanche[3] = 'Pudim'
print(lanche)
lanche.append('Biscoito')
print(lanche)
lanche.sort()
print(lanche)
lanche.sort(reverse=True)
print(lanche)
print(f'Essa lista tem {len(lanche)} Elementos.')
lanche.insert(2, 'Cachorro quente')
print(lanche)
lanche.pop()
print(lanche)
lanche.pop(2)
print(lanche)
print(f'Essa lista tem {len(lanche)} Elementos.')
for i in lanche:
    print(i)


