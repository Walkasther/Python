#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    linha = '~' * len(msg)
    print(linha)
    print(msg)
    print(linha)


escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')