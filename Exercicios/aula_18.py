# teste = list()
# teste.append('Gustavo')
# teste.append('40')
# galera =list()
# galera.append(teste[:]) # com [:]faz a cópia da lista.
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste)#sem o [:] faz a ligação entre as listas.
#
# print(galera)
#
# galera2 = [['Joao', 19],['Ana', 33],['Joaquim', 13],['Maria', 45]]
# print(galera2[0][0])
# print(galera2[2][1])
# print(galera2[1][1])
# print('-' * 30)
# for p in galera2:
#     print(p)
# print('-' * 30)
# for p in galera2:
#     print(p[0])
# print('-' * 30)
# for p in galera2:
#     print(p[1])
# print('-' * 30)
# for p in galera2:
#     print(f'{p[0]} tem {p[1]} anos de idade.')
#
# galera3 = list()
# dados = list()
# totmai = totmen = 0
# print('\033[31m')
# for c in range (0,3):
#     dados.append(str(input('Nome: ')))
#     dados.append(int(input('Idade: ')))
#     galera3.append(dados[:])
#     dados.clear()
#
# print(galera3)
#
# for p in galera3:
#     if p[1] >= 21:
#         print(f'{p[0]} é maior de idade.')
#         totmai += 1
#     else:
#         print(f'{p[0]} é menor de idade')
#         totmen += 1
# print(f'Temos {totmai} maiores e {totmen} menores de idade.')
import random
a = sorted(random.sample(range(1,61),6))

print(a)