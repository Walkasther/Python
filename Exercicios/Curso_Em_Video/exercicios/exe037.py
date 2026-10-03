#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#-1 para binário
#-2 para octal
#-3 para hexadecimal

n = (input('Digite um número inteiro: ')).strip()
base = input('\033[97mEm qual a base numérica o número está? 1-Binario  2-Octal  3-Decimal  4-Hexadecimal: ')
n1 = None

#--------------------------------------------------------------------------

if base == '1' or base.lower() ==  'binario' or base.lower() == 'binário':
    base = 'Binário'
elif base == '2' or base.lower() == 'octal':
    base = 'Octal'
elif base == '3' or base.lower() == 'decimal':
    base = 'Decimal'
elif base == '4' or base.lower() == 'hexadecimal':
    base = 'Hexadecimal'
else:
    print('Escolha uma opção válida!')

#--------------------------------------------------------------------------

conversor = input(''
      '\033[4;31m1-Binário'
      '\n\033[4;32m2-Octal'
      '\n\033[4;35m3-Decimal'
      '\n\033[4;33m4-Hexadecimal'
      '\n\033[0;34mSelecione a base que deseja converter: ')
print('\033[42;97m', end='')

#--------------------------------------------------------------------------
if n.isnumeric():
    n1 = int(n)

#--------------------------------------------------------------------------

if conversor == '1' or conversor.lower() == 'binario' or conversor.lower() == 'binário':
    binario = n1
    if base == 'Octal':
        binario = int(n, 8)
        binario = format(binario, 'b')
    elif base == 'Decimal':
        binario = format(n1, 'b')
        #outra opção: binario = bin(n1)[2:]
    elif base == 'Hexadecimal':
        binario = int(n, 16)
        binario = format(binario, 'b')
    print (f'\033[41;97mO valor {n} em {base} convertido para Binário é: {binario}\033[m')

elif conversor == '2' or conversor.lower() == 'octal':
    octal = n1
    if base == 'Binário':
        octal = int(n, 2)
        octal = format(octal, 'o')
    elif base == 'Decimal':
        octal = format(n1, 'o')
        #outra opção: octal = oct(n1)[2:]
    elif base == 'Hexadecimal':
        octal = int(n, 16)
        octal = format(octal, 'o')
    print('\033[42;97mO valor {} em {} convertido para Octal é {}\033[m'.format(n, base, octal))

elif conversor == '3' or conversor.lower() == 'decimal':
    decimal = n1
    if base == 'Binário':
        decimal = int(n, 2)
    elif base == 'Octal':
        decimal = int(n, 8)
    elif base == 'Hexadecimal':
        decimal = int(n, 16)
    print('\033[45;97mO valor {} em {} convertido para Decimal é {}\033[m'.format(n, base, decimal))

elif conversor == '4' or conversor.lower() == 'hexadecimal':
    hexadecimal = n
    if base == 'Binário':
        hexadecimal = int(n, 2)
        hexadecimal = format(hexadecimal, 'X')
    elif base == 'Octal':
        hexadecimal = int(n, 8)
        hexadecimal = format(hexadecimal, 'X')
    elif base == 'Decimal':
        hexadecimal = format(n1, 'X')
        #outra opção: hexadecimal = hex(n1)[2:0]
    print('\033[43;97mO valor {} em {} convertido para Hexadecimal é {}\033[m'.format(n, base, hexadecimal))

else:
    print('Escolha uma opção válida.')
