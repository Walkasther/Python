# help(input)
# print(input.__doc__)

def contador(i,f,p):
    """
    :param i:número que inicia a contagem
    :param f: número que finaliza a contagem
    :param p: número que determina o passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(c, end=' ')
        c += p
    print('FIM!')


def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    :return: Sem retorno
    Função criada por Gustavo Guanabara do canal Curso em Video
    """
    s = a + b + c
    print('A soma vale', s)


somar(3,4)
# help(contador)