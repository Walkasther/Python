#Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a digitação de um número de tipo inválido.
#Aproveite e crie também uma função leiafloat() com a mesma funcionalidade

def leiaint(legenda='Digite um número inteiro: ', positivo=False, negativo=False):
    """
        Recebe uma entrada contendo um número inteiro, se a entrada não for um número inteiro válido,
        a função notifica o usuário e pede novamente para digitar um número inteiro, até que seja válido.
        :param positivo: (Opcional) se True, só aceita valores positivos ou 0
        :param negativo: (Opcional) se True, só aceita valores negativos ou 0
        :param legenda: (Opcional) Tipo: Str → Texto de auxílio ao usuário
        :return: Número inteiro válido digitado pelo usuário
        """
    while True:
        try:
            entrada = int(input(legenda))

        except KeyboardInterrupt:
            print('\033[31m\nUsuário preferiu não digitar esse número.\033[m')
            return 0

        except ValueError:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')

        else:
            if positivo and not negativo:
                if entrada < 0:
                    print('\033[31mErro! Digite 0 ou um número inteiro positivo válido.\033[m')
                    continue

            if negativo and not positivo:
                if entrada > 0:
                    print('\033[31mErro! Digite 0 ou um número inteiro negativo válido.\033[m')
                    continue

            return entrada


def leiafloat(legenda='Digite um número real: ', positivo=False, negativo=False):
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
        try:
            entrada_str = input(legenda).replace(',','.')
            entrada = float(entrada_str)

        except KeyboardInterrupt:
            print('\033[31m\nUsuário preferiu não digitar esse número.\033[m')
            return 0

        except:
            print('\033[31mErro! Digite um número real válido.\033[m')

        else:
            if positivo and not negativo:
                if entrada < 0:
                    print('\033[31mErro! Digite 0 ou um número real positivo válido.\033[m')
                    continue

            if negativo and not positivo:
                if entrada > 0:
                    print('\033[31mErro! Digite 0 ou um número real negativo válido.\033[m')
                    continue

            return entrada


n = leiaint(positivo=True)
x = leiafloat(negativo=True)
print(f'Você digitou o númeno inteiro {n} e o número real {x}')