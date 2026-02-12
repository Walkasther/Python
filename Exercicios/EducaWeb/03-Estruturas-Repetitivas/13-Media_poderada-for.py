# Leia um valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de
# teste consiste de 3 valores reais, para os quais você deverá calcular e mostrar a média ponderada, sendo
# que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5. Vale lembrar
# que a média ponderada é a soma de todos os valores multiplicados pelo seu respectivo peso, dividida
# pela soma dos pesos.

n = int(input('Quantos casos voce vai digitar? '))

for _ in range(n):
    print('Digite três números: ')
    a = float(input())
    b = float(input())
    c = float(input())

    media = (a * 2 + b * 3 + c* 5) / 10

    print(f'MÉDIA = {media:.1f}')