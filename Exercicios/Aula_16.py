lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)#mostra todos os elementos da tupla
print(lanche[1])#mostra o elemento que está na posição 1, nesse caso é o suco
print(lanche[-3])#mostra o elemento que está no menos 3, nesse caso é o suco
print(lanche[1:3])#vai do 1 ate o 2
print(lanche[2:])#vai do 2 ate o final
print(lanche[:2])#vai do início até o 1
print(lanche[-2:])#vai do menos 2 até o final
#Tuplas são imutáveis
print('\033[31m')
# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# print('Comi pra caramba!')
del(lanche)#Deleta a tupla inteira.
for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')