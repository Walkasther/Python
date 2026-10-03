#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
#separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.

lista = [[],[]]

for i in range(0,7):
    valor2 = int(input(f'Digite o {i + 1}° valor:'))

    if valor2 % 2 == 0:
        lista[0].append(valor2)
    else:
        lista[1].append(valor2)

print('-=' * 30)
print(f'\033[34mOs valores pares digitados foram: {sorted(lista[0])}')
print(f'\033[36mOs valores impares digitados foram: {sorted(lista[1])}')