#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista_valores = []
while True:
    lista_valores.append(input('Digite um valor numérico. [N para sair]: '))
    if lista_valores[-1] in 'nN':
        lista_valores.pop()
        break
    if lista_valores[-1] in lista_valores[:-1]:
         print('Valor Duplicado, não vou adicionar...')
         lista_valores.pop()
lista_valores.sort()
print('\033[32m-' * 40)
print(f'Os valores digitados foram: {lista_valores}')

#Solução 2
lista_valores = []
while True:
    valor = (int(input('Digite um número: ')))
    continuar = input('Quer continuar? [S/N]: ')
    if valor  not in lista_valores:
        lista_valores.append(valor)
        print('Número adicionado com sucesso...')
    else:
        print('Valor Duplicado, não vou adicionar...')
    if continuar in 'nN':
        break
lista_valores.sort()
print('\033[31m-' * 40)
print(f'OS VALORES DIGITADOS FORAM: {lista_valores}')