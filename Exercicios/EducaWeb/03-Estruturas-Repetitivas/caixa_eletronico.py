print('Notas disponíveis: 100, 50, 20, 10, 5, 2, 1')

while True:
    valor_a_sacar = int(input('Digite um valor para sacar: '))
    cont = 0

    if not valor_a_sacar:
        print('Obrigado por usar o nosso banco! Até a próxima!!!')
        break

    print('Retirando...')
    print('_' * 30)
    while True:
        cont += 1

        if cont == 1:
            nota = 100
        elif cont == 2:
            nota = 50
        elif cont == 3:
            nota = 20
        elif cont == 4:
            nota = 10
        elif cont == 5:
            nota = 5
        elif cont == 6:
            nota = 2
        elif cont == 7:
            nota = 1
        else:
            break

        qtd = valor_a_sacar // nota
        valor_a_sacar -= qtd * nota

        if qtd > 0: print(f'{qtd} Notas de {nota} {"reais" if nota != 1 else "real"}')

    print('_' * 30)
