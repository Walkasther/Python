#Fazer um programa para ler o nome de um(a) Funcionário(a), o valor que ela recebe por hora, e a quantidade
#de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do funcionário com uma mensagem explicativa.

nome = input('Nome: ')
valor_hora = float(input('Valor por hora: '))
horas_trabalhadas = float(input('Horas trabalhadas: '))

pagamento = valor_hora * horas_trabalhadas

print(f'O pagamento para {nome} deve ser R$ {pagamento:.2f}')