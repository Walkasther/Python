#Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#-Equilátero: todos os lados iguais
#-Isósceles: dois lados iguais
#-Escaleno: todos os lados diferentes

a = float(input('Qual o valor da primeira reta? '))
b = float(input('Qual o valor da segunda reta? '))
c = float(input('Qual o valor da terceira reta? '))

if a + b > c and a + c > b and b + c > a:
    print('\033[32mCom essas retas é possível formar um triângulo', end=' ')
    if a == b == c:
        print('\033[35mEquilátero.')
    elif a != b != c != a:
        print('\033[33mEscaleno.')
    elif a == b or a == c  or b == c:
        print('\033[34mIsósceles.')
else:
    print('\033[31mCom essas retas não é possível formar um triângulo :(')
