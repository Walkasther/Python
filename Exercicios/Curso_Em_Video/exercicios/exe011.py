# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
#  necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

from Curso_Em_Video.Aulas import cores

largura = float(input(f'{cores.azul}Digite a largura: '))
altura = float(input(f'{cores.verde}Digite a altura: '))

area = largura * altura
tinta = area / 2

print('\033[36mPara pintar essa parede será preciso {:.2f} litros de tinta'.format(tinta))
