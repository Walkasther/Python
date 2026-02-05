def valida_pilha(expressao):
    pilha = []
    for c in expressao:
        if c == '(':
            pilha.append(c)
        elif c == ')':
            if not pilha:
                return False
            pilha.pop()

    return not pilha

expressao2 = input('Informe a expressão:')
print(valida_pilha(expressao2))