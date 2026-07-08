tupla_vogal = 'aula', 'python', 'codigo', 'variavel', 'lista', 'tupla', 'loop', 'condicao', 'funcao', 'classe', 'objeto', 'metodo', 'arquivo', 'dados', 'numero', 'texto', 'entrada', 'saida', 'logica', 'programa'

for palavra in tupla_vogal:
    print(f'Na palavra {palavra} temos ', end='')
    for vogal in palavra:
        if vogal in 'aeiouAEIOU':
            print(vogal, end = '')
    print()