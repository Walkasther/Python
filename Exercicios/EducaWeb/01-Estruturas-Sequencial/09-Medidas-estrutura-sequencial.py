#Fazer um programa para ler três medidas A, B e C. Em seguida, calcular e mostrar (imprimir os dados com quatro casas
#decimais):
#A) A área do quadrado que tem lado A
#B) A área do triângulo com base A e altura B
#C) A área do trápézio que tem bases A e B, e altura C

a = float(input('Digite a medida A: '))
b = float(input('Digite a medida B: '))
c = float(input('Digite a medida C: '))

area_quadrado = a ** 2
area_triangulo = (a * b) / 2
area_trapezio = (a + b) * c / 2

print(f'Área do quadrado: {area_quadrado:.4f}')
print(f'Área do triângulo: {area_triangulo:.4f}')
print(f'Área do trapézio: {area_trapezio:.4f}')
