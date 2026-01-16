#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
#usando while.

print('{:-^30}'.format('Progressão aritmetica'))
n = int (input('Informe o primeiro termo da PA: '))
r = int(input('Qual a razão da PA?'))
c = 0
print('\033[33mOS 10 primeiros termos dessa progressão aritmetica são:', end = '\n{')
while c < 10:
    print('{}'.format(n), end=(',' if c < 9 else '}'))
    n += r
    c += 1
