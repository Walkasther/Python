#Faça um programa que leia 5 valores numéricos e guarde numa lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista_valores = []
maior = 0
menor = 0
posicao_Maior = list()
posicao_Menor = []
for i in range (0,5):
    lista_valores.append(int(input(f'Digite o {i + 1}° valor:')))
    if i == 0:
        maior = lista_valores[i]
        menor = lista_valores[i]
        posicao_Maior.append(i)
        posicao_Menor.append(i)
    else:
        if maior < lista_valores[i]:
            maior = lista_valores[i]
            posicao_Maior.clear()
            posicao_Maior.append(i)
        else:
            if maior == lista_valores[i]:
                posicao_Maior.append(i)
            else:
                if menor > lista_valores[i]:
                    menor = lista_valores[i]
                    posicao_Menor.clear()
                    posicao_Menor.append(i)
                elif menor == lista_valores[i]:
                    posicao_Menor.append(i)

print('-' * 30)
print(f'Valores Digitados: {lista_valores}')
print('-' * 30)
print(f'O Maior valor digitado foi {maior} {'nas posições' if len(posicao_Maior) > 1 else 'na posição'}:', end=' ')
for c in posicao_Maior:
    print(c, end='\n' if c == posicao_Maior[-1] else ', ')

print(f'O Menor valor digitado foi {menor} {'nas posições' if len(posicao_Menor) > 1 else 'na posição'}:', end=' ')
for c in posicao_Menor:
    print(c, end=', ' if c != posicao_Menor[-1] else '')

