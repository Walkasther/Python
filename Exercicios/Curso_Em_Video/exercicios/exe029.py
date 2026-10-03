#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada km acima do limite.

v = input('\033[100mQual a velocidade que o carro estava? \033[m')
v2 = int(v)
if v2 > 80:
    print('Esse veiculo foi multado por passar da velocidade permitida.')
    multa = (v2 - 80) * 7
    print('O valor da multa foi de R$ {:.2f} Reais'.format(multa))
else:
    print('O Veiculo estava dentro da velocidade permitida.')
print('Tenha um bom dia! Dirija com segurança!')