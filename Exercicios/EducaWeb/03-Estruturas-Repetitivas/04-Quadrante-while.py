# Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no
# sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence (Q1, Q2, Q3 ou Q4). O
# algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem
# escrever mensagem alguma).

while True:
    print('Digite os valores das coordenadas X e Y:')
    x = float(input('X: '))
    y = float(input('Y: '))

    if x == 0 or y == 0:
        break

    if x > 0 and y > 0:
        quadrante = 'Quadrante Q1'

    elif x < 0 and y > 0:
        quadrante = 'Quadrante Q2'

    elif x < 0 and y < 0:
        quadrante = 'Quadrante Q3'

    else:
        quadrante = 'Quadrante Q4'

    print(quadrante)