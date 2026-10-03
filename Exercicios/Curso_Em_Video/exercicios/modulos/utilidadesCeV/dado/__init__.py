def leia_dinheiro(legenda='', positivo=False, negativo=False):
    """
    Recebe uma entrada contendo um número REAL, se a entrada não for um número REAL válido,
    a função notifica o usuário e pede novamente para digitar um número REAL, até que seja válido.

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
            ponto = False
            posicao_ponto = None

            if entrada[0] in '+-':
                if len(entrada) == 1:
                    print(f'\033[31mERRO! {entrada} é um preço inválido!\nDigite um valor válido para dinheiro.\033[m')
                    continue

                if entrada[0] == '-':
                    sinal_negativo = True

                entrada = entrada[1:]

                if entrada[0] in '+-':
                    print(f'\033[31mERRO! {entrada} é um preço inválido!\nDigite um valor válido para dinheiro.\033[m')
                    continue

            if '.' in entrada and ',' in entrada:
                print('\033[31mERRO! Entrada inválida!\nDigite um número real válido.\033[m')
                continue

            if '.' in entrada and entrada.count('.') == 1:
                ponto = True
                posicao_ponto = entrada.find('.')
                entrada = entrada[0:posicao_ponto] + entrada[posicao_ponto+1:]

            if ',' in entrada and entrada.count(',') == 1:
                ponto = True
                posicao_ponto = entrada.find(',')
                entrada = entrada[0:posicao_ponto] + entrada[posicao_ponto+1:]


            if entrada.isnumeric():
                if ponto:
                    entrada = entrada[0:posicao_ponto] + '.' + entrada[posicao_ponto:]

                if sinal_negativo:
                    entrada = -float(entrada)
                else:
                    entrada = float(entrada)

                if positivo and sinal_negativo:
                    print(f'\033[31mERRO! {entrada} é um preço inválido!\nDigite apenas 0 ou um número real positivo válido para dinheiro.\033[m')
                    continue

                elif negativo and not sinal_negativo and entrada != 0:
                    print(f'\033[31mERRO! {entrada} é um preço inválido!\nDigite apenas 0 ou um número real negativo válido para dinheiro.\033[m')
                    continue

                break

        print(f'\033[31mERRO! {entrada} é um preço inválido!\nDigite um valor válido para dinheiro.\033[m')

    return entrada