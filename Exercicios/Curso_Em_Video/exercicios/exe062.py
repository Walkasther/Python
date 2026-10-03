#Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
#ele disser que quer mostrar 0 termos.
print(f'{'PROGRESSÃO ARITMETICA':-^30}')
n = int(input('Informe o primeiro termo: '))
r = int(input('Qual a razão? '))
c = 0
s = 10
mais_termos = 10
print('\033[36mOs 10 primeiros termos dessa PA são: \n{', end ='')
while c < mais_termos:
    print('%i' % n,end=',' if c < mais_termos - 1 else '}')
    n += r
    c += 1
    if c == mais_termos:
        opcao = input('\n\033[97mQuer mostrar mais termos? [S/N]: ').upper().strip()
        if opcao == 'S':
            mais_termos = int(input('Quantos termos quer mostrar?'))
            c = 0
            s += mais_termos
            if mais_termos > 0:
                print('\033[36mOs próximos %d termos dessa PA são: \n' % mais_termos, end='{')
print('Progressão encerrada com {} termos, Volte logo! :)'.format(s))
