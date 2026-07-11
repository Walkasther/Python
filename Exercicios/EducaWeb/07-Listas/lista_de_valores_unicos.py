valor_unico = []

while True:
    valor = int(input('Digite um valor: '))

    if valor in valor_unico:
        print('\033[31mNúmero já adicionado!\033[m')

    else:
        valor_unico.append(valor)
        print('\033[32mAdicionado com Sucesso...\033[m')

    continuar = int(input('\033[30;44mQuer continuar? [1]SIM | [0]NÃO:\033[m '))

    if continuar == 0:
        break

print(f'Os valores da lista são: {sorted(valor_unico)}')