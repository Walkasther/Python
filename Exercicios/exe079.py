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
         lista_valores.pop()
lista_valores.sort()
print('\033[32m-' * 40)
print('Os valores digitados foram:', end='[')
for c in lista_valores:
    print(c, end= ']\n' if c == lista_valores[-1] else ',')

lista_valores = []
while True:
    valor = (int(input('Digite um número: ')))
    continuar = input('Quer continuar? [S/N]: ')
    if valor  not in lista_valores:
        lista_valores.append(valor)
    if continuar in 'nN':
        break
lista_valores.sort()
print('\033[31m-' * 40)
print('OS VALORES DIGITADOS FORAM:', end='[')
for c in lista_valores:
    print(c, end=']' if c == lista_valores[-1] else ', ')
