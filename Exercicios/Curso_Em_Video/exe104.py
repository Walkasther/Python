#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do python, só que fazendo
#a validação para aceitar apenas um valor numérico.
#EX: n = leiaInt('Digite um número: ')

def leia_int(n=''):
    """
    Recebe uma entrada contendo um número inteiro, se a entrada não for um número inteiro válido,
    a função notifica o usuário e pede novamente para digitar um número inteiro, até que seja válido.
    :param n: (Opcional) Tipo: Str → Texto de auxílio ao usuário
    :return: Número inteiro válido digitado pelo usuário
    """
    print('-' * 30)
    while True:
        a = input(n)
        if a:
            c = True

            if a[0] == '-':
                a = a[1:]
                c = False

            if a[0] == '+':
                a = a[1:]

            if a.isnumeric():
               if c:
                   a = int(a)
               else:
                   a = -int(a)
               break

        print('\033[31mERRO! Digite um número inteiro válido.\033[m')

    return a


def leia_float(n=''):
    """
    Recebe uma entrada contendo um número REAL, se a entrada não for um número REAL válido,
    a função notifica o usuário e pede novamente para digitar um número REAL, até que seja válido.

    Esta função aceita ',' no lugar do '.'

    :param n: (Opcional) Tipo: Str ⇾ Texto de auxílio ao usuário.
    :return: Número REAL válido digitado pelo usuário.
    """
    while True:
        a = input(n)
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

                break

        print('\033[31mERRO! Digite um número real válido.\033[m')

    return a


#Inicio do programa
n_inteiro = leia_int('Digite um número inteiro: ')
f = leia_float('Digite um número real: ')
print(f'Você digitou o número inteiro {n_inteiro}')
print(f'Você digitou o número Real {f}')

help(leia_int)
help(leia_float)