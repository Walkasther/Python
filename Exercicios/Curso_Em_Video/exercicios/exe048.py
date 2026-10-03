#Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que estão no
#intervalo de 1 até 500.

soma = 0
for c in range (1,501):
    print('\033[32m.',end='')
    if c % 3 == 0 and c % 2 == 1:
        soma += c
print('\033[33mA soma de todos os números impares múltiplos de 3 indo de 1 até 500 é: %d' % soma)

#solução 2, custa menos processamento do processador
soma2 = 0
quant = 0
for c in range (3,501,6):
    print('\033[34m.', end='')
    quant += 1
    soma2 += c
print('\033[33mA soma de todos os %i números impares múltiplos de 3 indo de 1 até 500 é: %d' % (quant, soma2))

