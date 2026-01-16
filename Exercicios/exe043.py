#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo:
#-Abaixo de 16: Baixo peso (grau 1)
#-Entre 16 e 16.99: Baixo peso (grau 2)
#-Entre 17 de 18.49: Baixo peso (grau 3)
#-Entre 18.5 e 24.99: Peso adequado
#-Entre 25 e 29.99: Sobrepeso
#-Entre 30 e 34.99: Obesidade Mórbida (grau 1)
#-Entre 35 e 39.99: Obesidade Mórbida (grau 2)
#Acima de 40: Obesidade Mórbida (grau 3)

peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (M) '))
imc = peso / altura ** 2

print('O seu índice de massa corporal é {:.2f}'.format(imc))

if imc < 16:
    print('\033[31mVocê está com baixo peso (grau 1)')
elif imc < 17:
    print('\033[35mVocê está com baixo peso (grau 2)')
elif imc < 18.5:
    print('\033[33mVocê está com baixo peso (grau 3')
elif imc < 25:
    print('\033[32mParabéns, você está no seu peso ideal!')
elif imc < 30:
    print('\033[36mVocê está com sobrepeso.')
elif imc < 35:
    print('\033[93mVocê está com obesidade mórbida (grau 1)')
elif imc < 40:
    print('\033[95mVocê está com obesidade mórbida (grau 2)')
else:
    print('\033[91mCuidado! você está com obesidade mórbida (grau 3)')
