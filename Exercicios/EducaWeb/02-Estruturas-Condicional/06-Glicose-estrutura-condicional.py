# Fazer um programa para ler a quantidade de glicose no sangue de uma pessoa e depois mostrar na tela a classificação
# desta glicose de acordo com essas referências:
#Normal - Até 100 mg/dl
#Elevado - Maior que 100 Até 140 mg/dl
#Diabetes - Maior que 140 mg/dl

glicose = float(input('Digite a medida da glicose: '))

if glicose < 0:
    print('Valor inválido!')
else:
    classificacao = 'Normal'

    if 100 < glicose <= 140:
        classificacao = 'Elevado'
    elif glicose > 140:
        classificacao = 'Diabetes'

    print(f'Classificação: {classificacao}')
