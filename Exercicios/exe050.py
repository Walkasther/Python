# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
#digitado for impar, desconsidere-o.

c1 = 0
soma = 0
for c in range (0,6):
    n = int(input('digite o {}° número inteiro: '.format(c+1)))
    if n % 2 == 0:
        soma += n
        c1 += 1
print(('foram digitados {} números pares.\nA soma dos números pares digitados é: {}'.format(c1, soma)))