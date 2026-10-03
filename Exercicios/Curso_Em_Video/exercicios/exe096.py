#Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retângular (largura e comprimento)
#e mostre a área do terreno.

def area(a,b):
    total = a * b
    print(f'A área de um terreno {a}x{b} é de {total}m²')


print('Controle dos terrenos')
print('-'*30)

largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))

area(largura,comprimento)