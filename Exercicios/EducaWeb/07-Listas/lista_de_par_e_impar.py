lista_par_impar = [[],[]]

for i in range(7):
    valor = int(input(f'Digite o {i+1}° valor: '))

    if valor % 2 == 0:
        if len(lista_par_impar[0]) == 0 or valor >= lista_par_impar[0][-1]:
            lista_par_impar[0].append(valor)
        else:
            for pos,par in enumerate(lista_par_impar[0]):
                if valor < par:
                    lista_par_impar[0].insert(pos, valor)
                    break

    else:
        if len(lista_par_impar[1]) == 0 or valor > lista_par_impar[1][-1]:
            lista_par_impar[1].append(valor)
        else:
            for pos,impar in enumerate(lista_par_impar[1]):
                if valor < impar:
                    lista_par_impar[1].insert(pos, valor)
                    break

print(f'\033[33mA lista completa é: {lista_par_impar}')
print(f'\033[31mA lista de pares é: {lista_par_impar[0]}')
print(f'\033[32mA lista de impares é: {lista_par_impar[1]}')