# Escreva um programa que leia um valor em metros e o exiba em centímetros e milímetros
from cores import magenta, reset

metros = float(input('{}Quantos metros quer converter?{} '.format(magenta, reset)))
centimetros = metros * 100
milimetros = centimetros * 10

print('Centímetros: {} \nMilímetros: {}'.format(centimetros,milimetros))