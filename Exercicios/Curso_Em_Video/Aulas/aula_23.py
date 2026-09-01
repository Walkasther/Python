#Try except

try:
    x = int(input('numero: '))
    print(x)

    a = int(input('Numerador: '))
    b = int(input('Denominador: '))

    r = a / b

except (ValueError, TypeError):
    print('Ocorreu um erro com o valor que você digitou, não é compatível')

except Exception as erro:
    print('\033[31mInfelizmente tivemos um problema :(\033[m')
    print(f'O problema encontrado foi: {erro.__class__}')

else:
    print(f'O resultado é {r:.2f}')

finally:
    print('Volte sempre!')