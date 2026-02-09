#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
#separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.

# lista_impar, lista_par, lista_geral = list(),list(),list()
# for i in range(0,7):
#     valor = int(input(f'Digite o {i+1}° valor: '))
#     if valor % 2 == 0:
#         lista_par.append(valor)
#     else:
#         lista_impar.append(valor)
# lista_geral.append(lista_par[:])
# lista_geral.append(lista_impar[:])
# del lista_impar
# del lista_par
# print('-=' * 30)
# print(f'\033[34mOs valores pares digitados foram: {sorted(lista_geral[0])}')
# print(f'\033[35mOs valores impares digitados foram: {sorted(lista_geral[1])}')

#Solução 2
lista = [[],[]]

for i in range(0,7):
    valor2 = int(input(f'Digite o {i + 1}° valor:'))
    if valor2 % 2 == 0:
        lista[0].append(valor2)
    else:
        lista[1].append(valor2)

print('-=' * 30)
print(lista)
print(f'\033[34mOs valores pares digitados foram: {sorted(lista[0])}')
print(f'\033[36mOs valores impares digitados foram: {sorted(lista[1])}')