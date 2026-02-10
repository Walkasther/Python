# No arremesso de dardo, o atleta tem três chances para lançar o dardo à maior distância que conseguir.
# Você deve criar um programa para, dadas as medidas das três tentativas de lançamento, informar qual
# foi a maior.

print('Digite as três distâncias:')
distancia1 = float(input())
distancia2 = float(input())
distancia3 = float(input())

maior = distancia1

if maior < distancia2:
    maior = distancia2

if maior < distancia3:
    maior = distancia3

print(f'MAIOR DISTÂNCIA = {maior:.2f}')
