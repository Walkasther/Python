def leia_int(legenda='Digite um número inteiro', positivo=False, negativo=False, minimo=None, maximo=None, cor=False):
    """
        Recebe uma entrada contendo um número inteiro, se a entrada não for um número inteiro válido,
        a função notifica o usuário e pede novamente para digitar um número inteiro, até que seja válido.

        :param maximo: (Opcional) determina qual é o valor máximo permitido digitado peço usuário.
        :param minimo: (Opcional) determina qual é o valor minimo permitido digitado peço usuário.
        :param positivo: (Opcional) se True, só aceita valores positivos ou 0.
        :param negativo: (Opcional) se True, só aceita valores negativos ou 0.
        :param legenda: (Opcional) Tipo: Str → Texto de auxílio ao usuário.
        :param cor: (Opcional) se True, deixa a legenda com cor personalizada alternativa

        :return: Número inteiro válido digitado pelo usuário.
        """

    from exercicios.modulos import print_formatado, entrada_personalizada
    if legenda == 'Digite um número inteiro' and positivo and not negativo:
        legenda += ' positivo: '

    elif legenda == 'Digite um número inteiro' and negativo and not positivo:
        legenda += ' negativo: '

    elif legenda == 'Digite um número inteiro':
        legenda += ': '

    while True:
        try:
            if cor:
                entrada = int(entrada_personalizada(legenda))

            else:
                entrada = int(input(legenda))

        except KeyboardInterrupt:
            print_formatado('\nUsuário preferiu não digitar esse número.', 'vermelho')
            return 0

        except ValueError:
            print_formatado('ERRO! Digite um número inteiro válido.', tipo='erro')

        else:
            if positivo and not negativo:
                if entrada < 0:
                    print_formatado('ERRO! Digite 0 ou um número inteiro positivo válido.', tipo='erro')
                    continue

            if negativo and not positivo:
                if entrada > 0:
                    print_formatado('erro! Digite 0 ou um número inteiro negativo válido.', tipo='erro')
                    continue

            if minimo is not None and entrada < minimo:
                print_formatado('ERRO! Valor Digitado fora do intervalo numérico permitido.', tipo='erro')
                print_formatado(f'Valor mínimo permitido -> {minimo}', tipo='aviso')
                continue

            if maximo is not None and entrada > maximo:
                print_formatado('ERRO! Valor Digitado fora do intervalo numérico permitido.', tipo='erro')
                print_formatado(f'Valor máximo permitido -> {maximo}', tipo='aviso')
                continue

            return entrada


def leia_float(legenda='Digite um número real', positivo=False, negativo=False, minimo=None, maximo=None, cor=False):
    """
    Recebe uma entrada contendo um número REAL, se a entrada não for um número REAL válido,
    a função notifica o usuário e pede novamente para digitar um número REAL, até que seja válido.

    Esta função aceita ',' no lugar do '.'

    :param maximo: (Opcional) determina qual é o valor máximo digitado peço usuário.
    :param minimo: (Opcional) determina qual é o valor minimo digitado peço usuário.
    :param legenda: (Opcional) Tipo: Str ⇾ Texto de auxílio ao usuário.
    :param positivo: (Opcional) se True, só aceita valores positivos ou 0
    :param negativo: (Opcional) se True, só aceita valores negativos ou 0
    :param cor: (Opcional) se True, deixa a legenda com cor personalizada alternativa

    :return: Número REAL válido digitado pelo usuário.
    """
    from exercicios.modulos import print_formatado, entrada_personalizada
    if legenda == 'Digite um número real' and positivo and not negativo:
        legenda += ' positivo: '

    elif legenda == 'Digite um número real' and negativo and not positivo:
        legenda += ' negativo: '

    else:
        legenda += ': '

    while True:
        try:
            if cor:
                entrada_str = entrada_personalizada(legenda).replace(',', '.')
            else:
                entrada_str = input(legenda).replace(',','.')

            entrada = float(entrada_str)

        except KeyboardInterrupt:
            print_formatado('\nUsuário preferiu não digitar esse número.', 'vermelho')
            return 0

        except ValueError:
            print_formatado('ERRO! Digite um número real válido.', tipo='erro')
            continue

        else:
            if positivo and not negativo:
                if entrada < 0:
                    print_formatado('ERRO! Digite 0 ou um número real positivo válido.', tipo='erro')
                    continue

            if negativo and not positivo:
                if entrada > 0:
                    print_formatado('ERRO! Digite 0 ou um número real negativo válido.', tipo='erro')
                    continue

            if minimo is not None and entrada < minimo:
                print_formatado('ERRO! Valor Digitado fora do intervalo numérico permitido.', tipo='erro')
                print_formatado(f'Valor mínimo permitido -> {minimo}', tipo='aviso')
                continue

            if maximo is not None and entrada > maximo:
                print_formatado('ERRO! Valor Digitado fora do intervalo numérico permitido.', tipo='erro')
                print_formatado(f'Valor máximo permitido -> {maximo}', tipo='aviso')
                continue

            return entrada


def cabecalho(titulo='', linha='-', padrao=True, quantidade=30):
    """
    Escreve um cabeçalho personalizado na tela
    :param quantidade: (opcional) define o tamanho da linha que fica acima e abaixo do título
    :param titulo: Titulo do cabeçalho. Caso o usuário não coloque nada, será impresso apenas uma linha
    :param linha: Linha acima e abaixo do título do cabeçalho.
    :param padrao: Se True, exibe a linha com tamanho padrão de 30 caracteres, caso Else, exibe a linha com tamanho personalizado
                   de acordo co o tamanho do título.
    :return: None → sem retorno função não retorna nada
    """

    if padrao:
        linha *= quantidade
    else:
        if len(linha) == 1:
            linha *= (len(titulo) + 4)
        else:
            linha *= int((len(titulo) + 4) / len(linha))

    if titulo:
        print(linha)
        print(f'{titulo.center(len(linha))}')
        print(linha)
    else:
        print(linha)


def menu(*opcoes, titulo='MENU PRINCIPAL', linhaa='-', qtd=30, padrao=True):
    cabecalho(titulo=titulo, linha=linhaa, quantidade=qtd, padrao=padrao)

    for pos, opcao in enumerate(opcoes):
        print(f'\033[33m{pos+1}\033[m - \033[34m{opcao}\033[m')

    linha(linhaa, qtd)
    escolha = leia_int('\033[93mSua Opção: \033[m', minimo=1, maximo=len(opcoes))

    return escolha


def linha(linhaa='-', quantidade=30):
        linhaa *= quantidade
        print(linhaa)
