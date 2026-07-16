# valores = [int(input(f'Digite o {i+1}° valor: ')) for i in range(5)]
#
# for posicao,valor in enumerate(valores):
#     if posicao > 0:
#         pos = posicao - 1
#         while True:
#             if valor < valores[pos]:
#                 valores.insert(pos, valor)
#                 valores.pop(pos + 2)
#                 if pos > 0:
#                     pos -= 1
#             else:
#                 break
#
# print(valores)


# valores = []
#
# for i in range(5):
#     valor = (int(input(f'Digite o {i+1}° valor: ')))
#     if i == 0 or valor >= valores[i-1]:
#         valores.append(valor)
#         print('Adicionado ao final da fila...')
#     else:
#         j = 1
#         cadastro = False
#         pos = i
#         while True:
#             if valor < valores[i-j]:
#                 cadastro = True
#                 if i - j > 0:
#                     j += 1
#
#                 else:
#                     valores.insert(i-j, valor)
#                     pos = i - j
#                     break
#             else:
#                 if cadastro:
#                     valores.insert(i - j + 1, valor)
#                     pos = i - j + 1
#                 break
#         print(f'Adicionado na posição {pos} da lista...')
#
# print(valores)


valores = []

for i in range(5):
    valor = (int(input(f'Digite o {i+1}° valor: ')))
    if i == 0 or valor >= valores[-1]:
        valores.append(valor)
        print('Adicionado ao final da fila...')
    else:
        j = 0
        while True:
            if valor > valores[j]:
                j += 1
            else:
                valores.insert(j, valor)
                print(f'Adicionado na posição {j} da lista...')
                break

print(valores)