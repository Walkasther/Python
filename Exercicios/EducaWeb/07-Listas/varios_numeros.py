valores = []

while True:
    valores.append(int(input('Digite um número: ')))
    continuar = int(input('Quer continuar? [1]Sim [0]Não: '))

    if continuar == 0:
        break

print(f'Foram digitados {len(valores)} números.')
print(f'A lista de valores em ordem decrescente é: {sorted(valores, reverse=True)}')
if 5 in valores:
    print(f'O valor 5 foi digitado e está na posição {valores.index(5)} da lista')
else:
    print('O valor 5 não foi digitado.')