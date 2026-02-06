#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta
#de inserção (sem usar o sort()).
#No final, mostre a lista ordenada na tela.

n = []
for i in range(0,5):
    valor = int(input(f'Digite o {i+1}° valor: '))
    if i == 0 or valor > n[-1]:
        n.append(valor)
        print('Adicionado ao final da lista...')
    else:
        if valor <= n[-1]:
            cont = 1
            pos = 0
            while valor <= n[i - cont]:
                if i - cont >= 0:
                    cont += 1
                    pos += 1
                else:
                    break
            n.insert(i - pos, valor)
            print(f'Adicionado na posição {i - pos} da lista...')
print('-=' * 25)
print(f'Os valores digitados em ordem foram: {n}')


#solução2
import bisect
numbers = []
for i in range(5):
    n = int(input('Type a number: '))
    bisect.insort(numbers, n)
    print(f'Number {n} included in position {numbers.index(n)}')
print(f'Numbers typed: numbers')