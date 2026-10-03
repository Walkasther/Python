#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
#O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from modulo_exe115 import *
from modulos.uteis import cabecalho, leia_int, menu

if not arquivo_existe('dados.txt'):
    criar_arquivo('dados.txt')

while True:

    opcao = menu('Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema', titulo='MENU PRINCIPAL',qtd=50, linhaa='-')

    if opcao==1:
        ler_arquivo('dados.txt')

    elif opcao==2:
        cabecalho('CADASTRAR PESSOA',quantidade=50)
        editar_arquivo(input('Nome: '), leia_int('Idade: '))

    elif opcao == 3:
        cabecalho('Saindo do sistema... Até logo!', quantidade=50)
        break