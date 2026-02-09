#Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 a 50.

print('Os números pares entre 1 e 50 são:')
for c in range(1,51):
    if c % 2 == 0:
        print(c, end=' ')
print('Acabou!')

#Solução 2. Exige menos do processador da máquina
for i in range(2,51,2):
    print(i, end=' ')