# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações sobre ele.
from cores import azul

algo = input('Digite algo: ')

print(azul)
print('Tipo primitivo: ',type(algo))
print('É alfa-numerico? ', algo.isalnum())
print('É alfabético? ', algo.isalpha())
print('É um número? ', algo.isnumeric())
print('É tudo maiúsculo? ', algo.isupper())
print('É somente espaço? ', algo.isspace())
print('É tudo minusculo? ', algo.islower())
print('É ascii? ', algo.isascii())
print('É decimal? ', algo.isdecimal())
print('É um digito? ', algo.isdigit())
print('É um identificador válido? ', algo.isidentifier())
print('Todos os caracteres são imprimíveis? ', algo.isprintable())
print('Está no formato Title Case? ', algo.istitle())
