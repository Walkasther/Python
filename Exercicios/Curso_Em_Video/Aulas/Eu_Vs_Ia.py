#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
# se a expressão passada está com os parenteses abertos e fechados na ordem correta.

#expressao = input('Digite a expressão: ')





def valida_sua(expressao):
    lista_expressao = []
    correto = True
    for i in expressao:
        lista_expressao.append(i)
    contador = 0
    if lista_expressao.count('(') != lista_expressao.count(")"):
        correto = False
    else:
        for i, c in enumerate(lista_expressao):
            if i == 0:
                if c == ')':
                    correto = False
                    break
                if c == '(':
                    contador += 1
                    if not lista_expressao[i + 1].isalnum():
                        if lista_expressao[i + 1] not in '(-)':
                            correto = False
                            break



            elif i == len(lista_expressao) - 1:
                if c == '(':
                    correto = False
                    break
                if c == ')':
                    contador -= 1
                    if not lista_expressao[i - 1].isalnum():
                        if lista_expressao[i - 1] not in '()':
                            correto = False
                            break



            else:
                if c == ')':
                    contador -= 1
                    if not lista_expressao[i - 1].isalnum():
                        if lista_expressao[i - 1] not in '()':
                            correto = False
                            break

                if c == '(':
                    contador += 1
                    if not lista_expressao[i + 1].isalnum():
                        if lista_expressao[i + 1] not in '(-)':
                            correto = False
                            break

                if contador < 0:
                    correto = False
                    break

    if contador != 0:
        correto = False
    return correto == True






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



from itertools import product

def gerar_expressões(tamanho):
    for p in product('()', repeat=tamanho):
        yield ''.join(p)






def testar(max_tamanho=8):
    for tamanho in range(1, max_tamanho + 1):
        for expr in gerar_expressões(tamanho):
            sua = valida_sua(expr)
            correta = valida_pilha(expr)

            if sua != correta:
                print('⚠️ Diferença encontrada!')
                print('Expressão:', expr)
                print('Sua lógica:', sua)
                print('Pilha:', correta)
                return

    print('✅ Nenhuma diferença encontrada até tamanho', max_tamanho)


testar(10)
