# Deseja-se converter uma medida de temperatura da escala Celsius para Fahrenheit ou vice-versa. Para
# isso, você deve construir um programa que leia a letra "C" ou "F" indicando em qual escala vai ser
# informada uma temperatura. Em seguida o programa deve mostrar a temperatura na outra escala com
# duas casas decimais. A seguir é dada a fórmula para converter de Fahrenheit para Celsius (você deve
# deduzir a fórmula de Celsius para Fahrenheit): C = 5 / 9 (F-32)

escala = input('Voce vai digitar a temperatura em qual escala (C/F)? ').strip().upper()[0]

if escala  in 'CF':
    nome_entrada = 'Celsius' if escala == 'C' else 'Fahrenheit'

    temperatura = float(input(f'Digite a temperatura em {nome_entrada}: '))

    if escala == 'C':
        temperatura_convertida = 9 / 5 * temperatura + 32
        nome_saida = 'Fahrenheit'

    elif escala == 'F':
        temperatura_convertida = 5 / 9 * (temperatura - 32)
        nome_saida = 'Celsius'

    print(f'Temperatura equivalente em {nome_saida}: {temperatura_convertida:.2f}')
else:
    print('Digite uma opção válida.')