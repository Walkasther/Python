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
        a = input(legenda)
        if a:
            sinal_negativo = False
            ponto = False
            posicao_ponto = int

            if a[0] == '-':
                sinal_negativo = True
                a = a[1:]

            if a[0] == '+':
                a = a[1:]


            if '.' in a and a.count('.') == 1:
                ponto = True
                posicao_ponto = a.find('.')
                a = a[0:posicao_ponto] + a[posicao_ponto+1:]

            if ',' in a and a.count(',') == 1:
                ponto = True
                posicao_ponto = a.find(',')
                a = a[0:posicao_ponto] + a[posicao_ponto+1:]


            if a.isnumeric():
                if ponto:
                    a = a[0:posicao_ponto] + '.' + a[posicao_ponto:]

                if sinal_negativo:
                    a = -float(a)
                else:
                    a = float(a)

                if positivo and sinal_negativo:
                    print(f'\033[31mERRO! {a} é um preço inválido!\nDigite apenas 0 ou um número real positivo válido para dinheiro.\033[m')
                    continue

                elif negativo and not sinal_negativo and a != 0:
                    print(f'\033[31mERRO! {a} é um preço inválido!\nDigite apenas 0 ou um número real negativo válido para dinheiro.\033[m')
                    continue

                break

        print(f'\033[31mERRO! {a} é um preço inválido!\nDigite um valor válido para dinheiro.\033[m')

    return a