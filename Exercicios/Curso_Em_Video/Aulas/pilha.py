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

# expressao = input('Informe a expressão:')
# pilha = []
# for c in expressao:
#     if c == '(':
#         pilha.append(c)
#     elif c == ')':
#         if not pilha:
#             pilha.append(c)
#             break
#         pilha.pop()
# if len(pilha) == 0:
#     print('Sua expressão está válida!')
# else:
#     print('sua expressão está errada!')

# expressão = input('Digite a expressão: ')
# if expressão.count('(') == expressão.count(')') and expressão.find('(') <= expressão.find(')'):
#     print('Sua expressão é valida')
# else:
#     print('Sua expressão não é valida')