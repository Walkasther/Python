def titulo(mensagem):
    print('-' * 30)
    print(f'{mensagem:^30}')
    print('-' * 30)


def soma(*a):
    soma_numeros = sum(a)
    print(f'A soma de {a} é {soma_numeros}')


def dobra(lst):
    pos = 0
    print(f'Os valores {lst} dobrados são:', end=' ')
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


def contagem(b):
    print(b)
    b += 4
    print(b)


#Programa principal
valores = [5,6,1,4]
x = 2

titulo('Somador de números')
soma(2,3,4)
soma(1,0,5)
soma(1,6)
dobra(valores)
print(valores)

contagem(x)
print(x)