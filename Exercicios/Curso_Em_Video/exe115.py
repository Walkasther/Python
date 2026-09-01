#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
#O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.


from modulos.uteis import cabecalho, leia_int

while True:
    cabecalho('MENU PRINCIPAL', quantidade=50)
    print(f'\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m')
    print(f'\033[33m2\033[m - \033[34mCadastrar nova Pessoa\033[m')
    print(f'\033[33m3\033[m - \033[34mSair do Sistema\033[m')
    cabecalho(quantidade=50)
    opcao = leia_int('\033[93mSua Opção: \033[m', minimo=1, maximo=3)

    if opcao==1:
        cabecalho('PESSOAS CADASTRADAS', quantidade=50)
        arquivo = open('dados.txt', 'r')
        conteudo = arquivo.read()
        print(conteudo)
        arquivo.close()

    elif opcao==2:
        cabecalho(quantidade=50)
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        arquivo = open('dados.txt', 'a')
        arquivo.write(f'{nome:<40}{idade} Anos\n')
        arquivo.close()

    elif opcao == 3:
        cabecalho('Saindo do sistema... Até logo!', quantidade=50)
        break