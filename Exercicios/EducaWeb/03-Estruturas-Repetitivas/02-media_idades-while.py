# Faça um programa para ler um número indeterminado de dados, contendo cada um, a idade de um
# indivíduo. O último dado, que não entrará nos cálculos, contém um valor de idade negativa. Calcular
# e imprimir a idade média deste grupo de indivíduos. Se for entrado um valor negativo na primeira vez,
# mostrar a mensagem "IMPOSSÍVEL CALCULAR".

soma_idade = 0
cont = 0

print('Digite as idades: ')

while True:
    idade = int(input())

    if idade < 0:
        if cont == 0:
            print('IMPOSSÍVEL CALCULAR')
        break

    soma_idade += idade
    cont += 1

if cont > 0:
    media = soma_idade / cont
    print(f'MÉDIA = {media:.2f}')