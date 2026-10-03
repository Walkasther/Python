# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se a pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.



def voto(ano_nascimento):
    """
    Esta função define se a idade atual está apta para votar, sendo obrigatório, opcional, ou não vota.
    :param ano_nascimento: Recebe a idade para ser analisada
    :return: String - 'OBRIGATÓRIO', 'OPCIONAL' ou 'NÃO VOTA'
    """
    from datetime import datetime

    idade = datetime.now().year - ano_nascimento
    if idade < 18:
        voto1 = 'NÃO VOTA'
    elif idade >= 65:
        voto1 = 'VOTO OPCIONAL'
    else:
        voto1 ='VOTO OBRIGATÓRIO'
    return f'Com {idade} anos: {voto1}'


print(voto(int(input('Em que ano você nasceu? '))))
