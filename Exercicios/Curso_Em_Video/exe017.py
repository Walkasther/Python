# Faça um programa que leia o comprimento de cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa.

from math import hypot

cateto_oposto = input('\033[33mQual o cateto oposto? ')
cateto_adjacente = input('\033[33mQual o cateto adjacente? ')
co = float(cateto_oposto)
ca = float(cateto_adjacente)

#Solução 1
hipotenusa = (co ** 2 + ca ** 2) ** 0.5
#Solução 2
#hipotenusa = hypot(co,ca)


print('\033[93mO comprimento da hipotenusa é {:.2f}'.format(hipotenusa))

