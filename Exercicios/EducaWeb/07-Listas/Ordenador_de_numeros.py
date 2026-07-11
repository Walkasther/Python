valores = [int(input(f'Digite o {i+1}° valor: ')) for i in range(5)]

for posicao,valor in enumerate(valores):
    if posicao > 0:
        pos = posicao - 1
        while True:
            if valor < valores[pos]:
                valores.insert(pos, valor)
                valores.pop(pos + 2)
                if pos > 0:
                    pos -= 1
            else:
                break

print(valores)


valores = []

for i in range(5):
    valor = (int(input(f'Digite o {i+1}° valor: ')))
    if i == 0 or valor >= valores[i-1]:
        valores.append(valor)
    else:
        j = 1
        cadastro = False
        while True:
            if valor < valores[i-j]:
                cadastro = True
                if i - j > 0:
                    j += 1
                else:
                    valores.insert(i-j, valor)
                    break
            else:
                if cadastro:
                    valores.insert(i - j + 1, valor)
                break

print(valores)