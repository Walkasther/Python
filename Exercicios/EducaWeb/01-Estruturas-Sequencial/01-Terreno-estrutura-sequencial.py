#Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular com uma casa decimal,
#bem como o valor do metro quadrado do terreno com duas casas decimais. Em seguida, o programa deve mostrar
#o valor da área do terreno, ambos com duas casas decimais.

largura = float(input('Qual a largura do terreno? '))
comprimento = float(input('Qual o comprimento do terreno? '))
valor_metro_quadrado = float(input('Qual o valor do metro quadrado? R$'))

area = largura * comprimento
valor_terreno = area * valor_metro_quadrado

print(f'Área do terreno = {area:.2f}')
print(f'Preço do terreno = R${valor_terreno:.2f}')