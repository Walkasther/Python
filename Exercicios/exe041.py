#A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
#categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 20 anos: SENIOR
#Acima de 20: MASTER

from datetime import date

idade = date.today().year - int(input('Olá atleta! informe o seu ano de nascimento com 4 dígitos: '))

if 9 >= idade >= 0:
    print('Você tem {} anos! A sua categoria é \033[31mMIRIM'.format(idade))
elif 14 >= idade >= 0:
    print('Você tem %d anos! A sua categoria é \033[32mINFANTIL' % idade)
elif 19 >= idade >= 0:
    print('Você tem %i anos! A Sua categoria é \033[33mJUNIOR' % idade)
elif 25 >= idade >= 0:
    print(f'Você tem {idade} anos! A sua categoria é \033[34mSENIOR')
elif idade > 25:
    print('Você tem',idade,'anos! A sua categoria é \033[35mMASTER')
else:
    print('\033[30;107mEsse ano nem chegou ainda! Por acaso você veio do futuro? haha\033[m')
