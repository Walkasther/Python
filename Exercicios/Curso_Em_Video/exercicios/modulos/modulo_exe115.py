from uteis import cabecalho


def criar_arquivo(nome):
    arquivo = open(nome, 'w')
    arquivo.close()
    print(f'Arquivo {nome} Criado com sucesso...')


def arquivo_existe(nome):
    try:
        arquivo = open(nome, 'r')
        arquivo.close()

    except FileNotFoundError:
        return False
    else:
        return True


def ler_arquivo(nome):
    try:
        cabecalho('PESSOAS CADASTRADAS', quantidade=50)
        arquivo = open(nome, 'r')

    except FileNotFoundError:
        print(f'\033[31mErro, Arquivo {nome} não encontrado!\033[m')

    else:
        conteudo = arquivo.read()
        print(conteudo)
        arquivo.close()


def editar_arquivo(nome='Desconhecido', idade=0):
    try:
        arquivo = open('Curso_Em_Video/exercicios/dados.txt', 'a')
        arquivo.write(f'{nome:<40}{idade:>3} Anos\n')
        arquivo.close()
        print('\033[32mNome Adicionado com Sucesso!\033[m')

    except Exception as erro:
        print('\033[31mERRO! Não foi possível adicionar.\033[m', erro)