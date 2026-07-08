valores = tuple(int(input(f'Digite o {x + 1}° valor: ')) for x in range(4))
p = 0

print(f'Você digitou os valores {valores}')
if 9 in valores:
    print(f'O número 9 apareceu {valores.count(9)} vezes')
else:
    print('O valor 9 não foi encontrado.')

if 3 in valores:
    print(f'O valor 3 foi digitado pela primeira vez na posição {valores.index(3)+1}')
else:
    print('O valor 3 não foi encontrado em nenhuma posição.')

for valor in valores:
    if valor % 2 == 0:
        p = 1
        break

if p == 1:
    print(f'Os números pares digitados foram: ', end='')
    for valor in valores:
        if valor % 2== 0:
            print(valor, end =' ')
else:
    print('Não foram encontrados valores pares.')