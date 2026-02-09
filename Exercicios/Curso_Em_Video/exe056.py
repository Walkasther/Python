#Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas. No final do programa, mostre:
#A média de idade do grupo.
#Qual o nome do homem mais velho.
#Quantas mulheres tem menos de 20 anos

nome = None
sexo = None
idade = None
mais_velho = None
media = 0
maior = 0
mulher_menor = 0

for i in range (0,4):
    nome = input(('Qual o nome da %i° pessoa: ' % (i + 1)))
    idade = int(input('Informe a idade: '))
    sexo = input('[M]Masculino \n[F]Feminino\nQual o sexo: ').lower()
    media += idade
    if idade > maior and sexo == 'm':
        maior = idade
        mais_velho = nome
    if idade < 20 and sexo == 'f':
       mulher_menor += 1

media = media / 4

print('Das 4 pessoas temos: '
      '\n\033[33mMédia de idade do grupo: %.0f anos.'
      '\n\033[34mHomem mais velho: %s com %i anos.'
      '\n\033[35mMulheres com menos de 20 anos: %d.' % (media, mais_velho,maior,mulher_menor))