#crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
#seu programa devera realizar a operação solicitada em cada caso.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
opcao = '0'
resultado = 0
t = None
while opcao != '8':
    opcao = str(input('[1]SOMAR'
          '\n[2]MULTIPLICAR'
          '\n[3]DIVIDIR'
          '\n[4]SUBTRAIR'
          '\n[5]MAIOR'
          '\n[6]MENOR'
          '\n[7]NOVOS NÚMEROS'
          '\n[8]SAIR'
          '\nEscolha uma opção: '))
    if opcao in ('1','2','3','4'):
        if opcao == '1':
            resultado = n1 + n2
            t = 'soma'
        elif opcao == '2':
            resultado = n1 * n2
            t = 'multiplicação'
        elif opcao == '3':
            resultado = n1 / n2
            t = 'divisão'
        elif opcao == '4':
            resultado = n1 - n2
            t = 'subtração'
        print('\033[36mO resultado da %s entre %d e %i é %.2f\033[m' % (t, n1, n2, resultado))
    elif opcao in ('5','6'):
        if opcao == '5':
            t = 'maior'
            if n1 > n2:
                resultado = n1
            elif n1 < n2:
                resultado = n2
        if opcao == '6':
            t = 'menor'
            if n1 > n2:
                resultado = n2
            elif n1 < n2:
                resultado = n1
        if n1 == n2:
            print('\033[91mNão existe valor %s, pois os dois valores são iguais.\033[m' %t)
        else:
            print('\033[34mO %s valor entre %d e %d é %d\033[m' % (t, n1, n2, resultado))
    elif opcao == '7':
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == '8':
        print('Finalizando...')
    else:
        print('\033[31mOpção invalida, tente novamente!!\033[m')
print('\033[33mPROGRAMA ENCERRADO!')