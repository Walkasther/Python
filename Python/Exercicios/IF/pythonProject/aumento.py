salario_atual = float(input("Digite o salario da pessoa: "))
novo_salario : float
aumento : float
porcentagem : float

if salario_atual <= 1000 :
    aumento = salario_atual * 20 / 100
    novo_salario = salario_atual + aumento
    porcentagem = aumento / salario_atual * 100
elif salario_atual <= 3000:
    aumento = salario_atual * 15 / 100
    novo_salario = salario_atual + aumento
    porcentagem = aumento / salario_atual * 100
elif salario_atual <= 8000 :
    aumento = salario_atual * 10 / 100
    novo_salario = salario_atual + aumento
    porcentagem = aumento / salario_atual * 100
else:
    aumento = salario_atual * 5 / 100
    novo_salario = salario_atual + aumento
    porcentagem = aumento / salario_atual * 100

print(f"Novo salario = R$ {novo_salario:.2f}")
print(f"Aumento = R$ {aumento:.2f}")
print(f"Porcentagem = {porcentagem} %")