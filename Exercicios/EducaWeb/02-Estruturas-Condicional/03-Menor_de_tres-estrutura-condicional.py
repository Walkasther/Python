# Fazer um programa para ler três números inteiros. Em seguida, mostrar qual o menor dentre os três
# números lidos. Em caso de empate, mostrar apenas uma vez.

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

menor = n1

if menor > n2:
    menor = n2

if menor > n3:
    menor = n3

print(f'MENOR = {menor}')