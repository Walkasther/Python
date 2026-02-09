# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Informe a temperatura em Celsius: '))
f = ((9 * c) / 5) + 32
print('\033[35mA temperatura de {:.2f}° celsius corresponde a {:.2f}°F'.format(c,f))
