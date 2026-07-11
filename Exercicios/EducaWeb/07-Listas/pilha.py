while True:
    pilha = 0
    expressao = input('Digite a expressão (zzz para sair): ')

    for caractere in expressao:
        if caractere == '(':
            pilha += 1
        elif caractere == ')' and pilha > 0:
            pilha -= 1
        elif caractere == ')' and pilha == 0:
            pilha -= 1
            break

    if pilha == 0:
        print('\033[92mSua expressão é válida!\033[m')
    else:
        print('\033[91mSua expressão está errada!\033[m')

    if expressao == 'zzz':
        break