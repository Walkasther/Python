# Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para
# organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano,
# quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este
# laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas
# informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia
# utilizada e a quantidade de cobaias utilizadas em cada experimento. Faça um programa que leia um
# valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um
# inteiro que representa a quantidade de cobaias utilizadas e uma letra ('C', 'R' ou 'S'), indicando o tipo
# de cobaia (R:Rato S:Sapo C:Coelho). Apresente o total de cobaias utilizadas, o total de cada tipo de
# cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o
# percentual deve ser apresentado com dois dígitos após o ponto.

n = int(input('Quantos casos de teste serao digitados? '))

cobaias_total = coelhos_total = ratos_total = sapos_total = 0

for _ in range(n):
    cobaias_quantidade = int(input('Quantidade de cobaias: '))
    cobaias_tipo = input('Tipo de cobaia: ').strip().upper()

    if cobaias_tipo in 'CRS':
        if cobaias_tipo == 'C':
            coelhos_total += cobaias_quantidade
        elif cobaias_tipo == 'R':
            ratos_total += cobaias_quantidade
        else:
            sapos_total += cobaias_quantidade

        cobaias_total += cobaias_quantidade
    else:
        print('Tipo invalido')

if cobaias_total > 0:
    percentual_coelhos = coelhos_total / cobaias_total * 100
    percentual_ratos = ratos_total / cobaias_total * 100
    percentual_sapos = sapos_total / cobaias_total * 100
else:
    percentual_coelhos = percentual_ratos = percentual_sapos = 0

print('RELATORIO FINAL')
print(f'Total: {cobaias_total} cobaias')
print(f'Total de coelhos: {coelhos_total}')
print(f'Total de ratos: {ratos_total}')
print(f'Total de sapos: {sapos_total}')
print(f'Percentual de coelhos: {percentual_coelhos:.2f}')
print(f'Percentual de ratos: {percentual_ratos:.2f}')
print(f'Percentual de sapos: {percentual_sapos:.2f}')
