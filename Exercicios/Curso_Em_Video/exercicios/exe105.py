#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as
#seguintes informações:
# -Quantidade de notas
# -A maior nota
# -A menor nota
# -A média da turma
# -A situação(opcional)

def notas(*notas1, sit=False):
    """
    Recebe várias notas e retorna um dicionário contendo dados da turma.
    :param notas1: Recebe uma ou várias notas
    :param sit: (opcional) tipo lógico, Exibe ou não a situação da turma com base na média das notas enviadas
    :return: dicionario com dados(total de notas, maior nota, menor nota, media da turma e situação (se sit for True)
    """
    turma = dict(total = len(notas1),
    maior = max(notas1),
    menor = min(notas1),
    )

    turma['media'] = float(f"{sum(notas1) / turma['total']:.2f}")

    if sit:
        if turma['media'] >= 7:
            turma['situacao'] = 'BOA'

        elif turma['media'] >= 5:
            turma['situacao'] = 'RAZOÁVEL'

        else:
            turma['situacao'] = 'RUIM'

    return turma


#Programa principal
resp = notas(3.5, 2, 6.5, 8.6, sit=True)
print(resp)