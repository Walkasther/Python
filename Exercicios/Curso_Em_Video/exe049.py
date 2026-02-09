#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.

n = int(input('Digite um número: '))
print('\033[97m{:+^25}'.format(' TABUADA do {} '.format(n)))
for c in range (0,11):
    print('\033[34m{:>6}  X  {:>2}  =  {}'.format(c, n, c * n))
