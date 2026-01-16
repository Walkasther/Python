# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

a = input('\033[30;100mQual o ângulo? ')
angulo = radians(float(a))
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)

print('O valor do seno é {:.2f}, do cosseno é {:.2f} e da tangente é {:.2f}'.format(seno,cosseno,tangente))

