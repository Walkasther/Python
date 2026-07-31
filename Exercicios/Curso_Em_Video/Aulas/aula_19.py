#Dicionários

dados = dict(nome = 'joão', idade = 23, peso = 97.5)
dados2 = {'Nome': 'Mateus', 'Idade': 28, 'Peso': 88.7 }

dados['altura'] = 1.60

lista_dados = [dados.copy()]
lista_dados.append(dados2.copy())

del(dados2['Idade'])

print(dados)
print(dados2)

for k in dados2.keys():
    print(k)
for k in dados2:
    print(k)

for v in dados2.values():
    print(v)

for k, v in dados2.items():
    print('O', k, 'é', v)