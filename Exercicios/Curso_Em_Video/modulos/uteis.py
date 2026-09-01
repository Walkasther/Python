def leia_int(legenda='', positivo=False, negativo=False):
    """
    Recebe uma entrada contendo um número inteiro, se a entrada não for um número inteiro válido,
    a função notifica o usuário e pede novamente para digitar um número inteiro, até que seja válido.
    :param positivo: (Opcional) se True, só aceita valores positivos ou 0
    :param negativo: (Opcional) se True, só aceita valores negativos ou 0
    :param legenda: (Opcional) Tipo: Str → Texto de auxílio ao usuário
    :return: Número inteiro válido digitado pelo usuário
    """
    print('-' * 30)
    while True:
        a = input(legenda).strip()
        if a:
            numero_positivo = True

            if a[0] == '-':
                a = a[1:]
                numero_positivo = False

            if a[0] == '+':
                a = a[1:]

            if a.isnumeric():
               if numero_positivo:
                   a = int(a)
               else:
                   a = -int(a)

               if positivo and not numero_positivo:
                   print('\033[31mERRO! Digite apenas 0 ou um número inteiro positivo válido.\033[m')
                   continue

               elif negativo and numero_positivo and a != 0:
                   print('\033[31mERRO! Digite apenas 0 ou um número inteiro negativo válido.\033[m')
                   continue

               break

        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return a


def leia_float(legenda='Digite um número Real: ', positivo=False, negativo=False):
    """
    Recebe uma entrada contendo um número REAL, se entrada entrada não for um número REAL válido,
    entrada função notifica o usuário e pede novamente para digitar um número REAL, até que seja válido.

    Esta função aceita ',' no lugar do '.'

    :param legenda: (Opcional) Tipo: Str ⇾ Texto de auxílio ao usuário.
    :param positivo: (Opcional) se True, só aceita valores positivos ou 0
    :param negativo: (Opcional) se True, só aceita valores negativos ou 0
    :return: Número REAL válido digitado pelo usuário.
    """
    while True:
        entrada = input(legenda).strip()
        if entrada:
            sinal_negativo = False
            tem_ponto = False
            posicao_ponto = None

            if entrada[0] in '+-':
                if len(entrada) == 1:
                    print(f'\033[31mERRO! Entrada inválida!\nDigite um número real válido.\033[m')
                    continue

                if entrada[0] == '-':
                    sinal_negativo = True

                entrada = entrada[1:]

                if entrada[0] in '+-':
                    print(f'\033[31mERRO! Entrada inválida!\nDigite um número real válido.\033[m')
                    continue

            if '.' in entrada and ',' in entrada:
                print('\033[31mERRO! Entrada inválida!\nDigite um número real válido.\033[m')
                continue

            if '.' in entrada and entrada.count('.') == 1:
                tem_ponto = True
                posicao_ponto = entrada.find('.')
                entrada = entrada[0:posicao_ponto] + entrada[posicao_ponto+1:]

            if ',' in entrada and entrada.count(',') == 1:
                tem_ponto = True
                posicao_ponto = entrada.find(',')
                entrada = entrada[0:posicao_ponto] + entrada[posicao_ponto+1:]


            if entrada.isnumeric():
                if tem_ponto:
                    entrada = entrada[0:posicao_ponto] + '.' + entrada[posicao_ponto:]

                if sinal_negativo:
                    entrada = -float(entrada)
                else:
                    entrada = float(entrada)

                if positivo and sinal_negativo:
                    print('\033[31mERRO! Digite apenas 0 ou um número real positivo válido.\033[m')
                    continue

                elif negativo and not sinal_negativo and entrada != 0:
                    print('\033[31mERRO! Digite apenas 0 ou um número real negativo válido.\033[m')
                    continue

                break

        print('\033[31mERRO! Digite um número real válido.\033[m')

    return entrada


def cabecalho(titulo='', linha='-', padrao=True, ):
    """
    Escreve um cabeçalho personalizado na tela
    :param titulo: Titulo do cabeçalho. Caso o usuário não coloque nada, será impresso apenas uma linha
    :param linha: Linha acima e abaixo do título do cabeçalho.
    :param padrao: Se True, exibe a linha com tamanho padrão de 30 caracteres, caso Else, exibe a linha com tamanho personalizado
                   de acordo co o tamanho do título.
    :return: está função não retorna nada
    """

    if padrao:
        linha *= 30
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