#Faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade:
#-Se ele ainda vai se alistar ao serviço militar.
#-Se é a hora de se alistar.
#-Se já passou do tempo do alistamento.

from datetime import date
sexo = input('[0] Masculino'
             '\n[1] Feminino'
             '\nQual o seu sexo? ')
if sexo == '0':
    data_atual = date.today().year
    nascimento = int(input('Informe o ano do seu nascimento com 4 dígitos: '))
    idade = data_atual - nascimento
    data_alistamento = 18 - idade + data_atual
    if 18 > idade >= 0:
        print('Você tem %i anos, portanto ainda não está na hora de se alistar! o seu alistamento está previsto para %d' % (idade, data_alistamento))
    elif idade == 18:
        print('Você tem %d anos, está na hora de se alistar!' % idade)
    elif idade > 18:
        print('Já passou da hora de se alistar campeão! Seu alistamento era para ter acontecido em %d, a %i anos atrás!' % (data_alistamento, (data_atual - data_alistamento)))
    else:
        print('Esse ano ainda nem chegou! Por acaso você veio do futuro? haha')
elif sexo == '1':
    print('Você não precisa se alistar no exército brasileiro.')
else:
    print('Digite uma opção válida!')