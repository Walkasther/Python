#Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são as vogais.

tupla_vogal = 'aula', 'python', 'codigo', 'variavel', 'lista', 'tupla', 'loop', 'condicao', 'funcao', 'classe', 'objeto', 'metodo', 'arquivo', 'dados', 'numero', 'texto', 'entrada', 'saida', 'logica', 'programa'
tupla2 = 1,2,3,4,5,6,7,89,9,10
for c, palavra in enumerate(tupla_vogal):
        print(f'Na palavra {palavra.upper()} temos: ',end='')
        for i in range(0,len(palavra)):
            if palavra[i].lower() in 'aeiou':
                print(palavra[i], end=' ')
        print()