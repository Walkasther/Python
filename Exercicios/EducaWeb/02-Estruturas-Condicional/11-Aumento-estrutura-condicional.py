# Uma empresa vai conceder um aumento percentual de salário aos seus funcionários dependendo de quanto cada pessoa
# ganha, conforme tabela ao lado. Fazer um programa para ler o salário de uma pessoa, daí mostrar qual o novo salário
# desta pessoa depois do aumento, quanto foi o aumento e qual foi a porcentagem de aumento conforme a tabela abaixo:
# Salário atual: Até R$ 1000 | Aumento: 20%
# Salário atual: Acima de 1000 e até R$ 3000 | Aumento: 15%
# Salário atual: Acima de 3000 e até R$ 8000 | Aumento: 10%
# Salário atual: Acima de R$ 8000 | Aumento: 5%

salario_atual = float(input('Digite o salário da pessoa: '))
porcentagem = 5

if salario_atual <= 1000:
    porcentagem = 20
elif 1000 < salario_atual <= 3000:
    porcentagem = 15
elif salario_atual <= 8000:
    porcentagem = 10

aumento = salario_atual * porcentagem / 100
novo_salario = salario_atual + aumento

print(f'Novo salário = R$ {novo_salario:.2f}')
print(f'Aumento = R$ {aumento:.2f}')
print(f'Porcentagem = {porcentagem}%')
