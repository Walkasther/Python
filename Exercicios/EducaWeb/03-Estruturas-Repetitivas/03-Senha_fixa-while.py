# Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de
# senha incorreta informada, escrever a mensagem "Senha Invalida! Tente novamente:". Quando a senha
# for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo
# encerrado. Considere que a senha correta é o valor 2002.

SENHA_CORRETA = 2002

while True:
    senha_digitada = int(input('Digite a senha: '))

    if senha_digitada == SENHA_CORRETA:
        print('Acesso Permitido!')
        break

    print('Senha Invalida! Tente novamente:')
