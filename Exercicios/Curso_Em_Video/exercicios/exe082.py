#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
#conter apenas os valores pares e os valores impares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.

lista_valores, lista_pares, lista_impares = [], [], []
while True:
    lista_valores.append(int(input('Digite um número: ')))
    cont = int(input('Quer continuar? [1]SIM [2]NÃO: '))
    if cont == 2:
        break

for c in lista_valores:
    if c % 2 == 0:
        lista_pares.append(c)
    else:
        lista_impares.append(c)
print('-=' * 25)
print(f'\033[33mA lista completa é: {lista_valores}')
print(f'\033[31mA lista de pares é: {lista_pares}')
print(f'\033[32mA lista de Impares é {lista_impares}')