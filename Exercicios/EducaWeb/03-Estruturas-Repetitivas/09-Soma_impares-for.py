# Leia 2 valores inteiros X e Y (em qualquer ordem). A seguir, calcule e mostre a soma dos números
# impares entre eles.

soma = 0

print('Digite dois números: ')
x = int(input())
y = int(input())


if x > y:
    x, y = y, x

if x % 2 == 0:
    x += 1
else:
    x += 2

for i in range(x, y, 2):
    soma += i

print(f'SOMA DOS IMPARES = {soma}')