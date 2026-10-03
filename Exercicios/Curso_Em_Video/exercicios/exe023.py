#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos seus dígitos separados.
#ex: Digite um numero: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

n1 = input('\033[34mDigite um número: ')
resultado = int(n1)

milhar = resultado // 1000
centena = (resultado - 1000 * milhar) // 100
dezena = (resultado - 1000 * milhar - 100 * centena) // 10
unidade = resultado - 1000 * milhar - 100 * centena - 10 * dezena

# u = resultado // 1 % 10
# d = resultado // 10 % 10
# c = resultado // 100 % 10
# m = resultado // 1000 % 10

print('\033[94mUnidade: {}'.format(unidade))
print('Dezena:  {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar:  {}'.format(milhar))
