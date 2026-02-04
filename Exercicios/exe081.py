#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

lista_valores = []
cont = 1
while True:
    lista_valores.append(int(input(f'Digite o {cont}° valor: ')))
    cont += 1
    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    print('-' * 30)
lista_valores.sort(reverse=True)
print('-=' * 15)
print(f'Foram digitados {len(lista_valores)} números.')
print(f'Os valores digitados foram {lista_valores}')
if 5 in lista_valores:
    print(f'O número 5 faz parte da lista e está na posição {lista_valores.index(5)}!')
else:
    print('O valor 5 não foi encontrado na lista!')
