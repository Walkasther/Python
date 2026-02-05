#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
# se a expressão passada está com os parenteses abertos e fechados na ordem correta.



expressao = input('Digite a expressão: ').strip()
expressao = ''.join(expressao.split())
print(expressao)
lista_expressao = []
correto = True
for i in expressao:
    lista_expressao.append(i)
contador = 0
if lista_expressao.count('(') != lista_expressao.count(")"):
    correto = False
else:
    for i,c in enumerate(lista_expressao):
        if i == 0:
            if c == ')' or c in '*/':
                correto = False
                break
            if c == '(':
                contador += 1
                if not lista_expressao[i+1].isalnum() :
                    if lista_expressao[i+1] not in '(-)':
                        correto = False
                        break



        elif i == len(lista_expressao) - 1:
            if c == '(' or c in '*/':
                correto = False
                break
            if c == ')':
                contador -= 1
                if not lista_expressao[i-1].isalnum():
                    if lista_expressao[i-1] not in '()':
                        correto = False
                        break



        else:
            if c == ')':
                contador -= 1
                if not lista_expressao[i-1].isalnum():
                   if lista_expressao[i-1] not in '()':
                        correto = False
                        break


            if c == '(':
                contador += 1
                if not lista_expressao[i+1].isalnum():
                    if lista_expressao[i+1] not in '(-)':
                        correto = False
                        break


            if contador < 0:
                correto = False
                break

if contador != 0:
    correto = False


if correto:
    print('A expressão está correta.')
else:
    print('A expressão está errada.')
