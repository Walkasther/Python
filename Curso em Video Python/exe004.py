diaria = float(input('qual o valor da diária?'))
km = float(input('qual o valor do km rodado?'))
qtd_dia = int(input('Por quantos dias o carro foi alugado?'))
qtk_km = int(input('quantos km foram rodados durante esse período?'))
total = diaria * qtd_dia + km * qtk_km

print('O total a pagar é de R$ {:.2f}'.format(total))