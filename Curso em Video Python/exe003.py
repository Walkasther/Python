l = float(input('qual a largura da parede? '))
a = float(input('Qual a altura da parede? '))
area = a * l
tinta = area / 2
print('Para pintar essa parede será preciso {:.2f} litros de tinta'.format(tinta))

preco = float(input('Qual o preço do produto? '))

print('O preço do produto com desconto de 5% é {:.2f}'.format(preco - preco * 5 / 100))

salario = float(input('Qual o salario antigo do funcionário?'))

print('o novo salario do funcionário é de {:.2f}'.format(salario + salario * 15 / 100))

dinheiro = float(input("quanto dinheiro você tem? "))
conversor = dinheiro / 5.69
print('{:.2f}'.format(conversor))