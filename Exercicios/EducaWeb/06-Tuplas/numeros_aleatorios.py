from random import sample

anumeros = tuple(sample(range(11),5))

print(f'Números gerados: {anumeros}')
print(f'Menor valor: {min(anumeros)}')
print(f'Maior valor: {max(anumeros)} ')