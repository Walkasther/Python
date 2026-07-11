tupla_vogal = 'aula', 'python', 'codigo', 'variavel', 'lista', 'tupla', 'loop', 'condicao', 'funcao', 'classe', 'objeto', 'metodo', 'arquivo', 'dados', 'numero', 'texto', 'entrada', 'saida', 'logica', 'programa'

for palavra in tupla_vogal:
    print(f'Na palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end ='')
    print()