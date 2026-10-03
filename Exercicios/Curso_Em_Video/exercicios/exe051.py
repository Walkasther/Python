#Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmetica. No final, mostre os 10 primeiros
#termos dessa progressão.

a1 = int(input('Digite o primeiro termo: '))
progressao = a1
r = int(input('Digite a razão: '))

ver = input('\033[97m[1]VER OS 10 PRIMEIROS TERMOS DESTA PROGRESSÃO'
            '\n[2]VER O TERMO DE DETERMINADA POSIÇÃO'
            '\n[3]VER A POSIÇÃO DE DETERMINADO TERMO '
            '\n[4]SAIR'
            '\nEscolha uma opção: ')
if ver == '1':
    if r > 0:
        print('\033[92mEssa é uma Progressão crescente. Os 10 primeiros termos dessa progressão são:')
    elif r == 0:
        print('\033[93mEssa é uma progressão constante. Os 10 primeiros termos dessa progressão são: ')
    elif r < 0:
        print('\033[91mEssa é uma razão decrescente. Os 10 primeiros termos dessa progressão são: ')
    print('(', end ='')
    for i in range (0,10):
        print (progressao, end=', ')
        progressao += r
    print(')')


elif ver == '2':
    termo = int(input('Qual o número da posição do termo que gostaria de ver? '))
    termo_especifico = a1 + (termo - 1) * r
    print('\033[94mO termo {} da progressão atual é: {}'.format(termo, termo_especifico))

elif ver == '3':
    posicao = int(input('Qual o termo que gostaria de ver a posição? '))
    posicao_especifica = int((posicao - a1 + r) / r)
    print('\033[94mO termo {} está na posição {} da progressão atual.'.format(posicao, posicao_especifica))
elif ver == '4':
    print('Ok! Obrigado.')
else:
    print('\033[31mEscolha uma opção válida!!!')


######################################################
# solução 2
termo2 = int(input('Informe o primeiro termo: '))
razao2 = int(input('Informe a razão: '))
decimo = termo2 + razao2 * 10
print('(',end='')
for i in range (termo2, decimo, razao2):
    print (i, end=', ')
print(')')