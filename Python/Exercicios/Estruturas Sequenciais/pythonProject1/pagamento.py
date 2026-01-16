nome = input("Nome: ")
valor_hora = float (input("Valor por hora: "))
hora_trabalhada = int(input("Horas trabalhadas: "))
pagamento = valor_hora * hora_trabalhada

print(f"O pagamento para {nome} deve ser {pagamento:.2f}")