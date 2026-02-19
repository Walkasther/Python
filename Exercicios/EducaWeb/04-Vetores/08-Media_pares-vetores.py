# Fazer um programa para ler um vetor de N números inteiros. Em seguida, mostrar na tela a média
# aritmética somente dos números pares lidos, com uma casa decimal. Se nenhum número par for
# digitado, mostrar a mensagem "NENHUM NÚMERO PAR"

n = int(input('Quantos elementos vai ter o vetor? '))
numeros = []

for _ in range(n):
    numeros.append(int(input('Digite um número: ')))

soma_pares = sum(i for i in numeros if i % 2 == 0)
cont_par = sum(1 for i in numeros if i % 2 == 0)

if cont_par > 0:
    media_pares = soma_pares / cont_par
    print(f'MEDIA DOS PARES = {media_pares:.1f}')
else:
    print('NENHUM NUMERO PAR')