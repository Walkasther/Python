investimento = float(input("Digite o valor inicial: "))
juros = float(input("Quanto de juros vai render? "))
periodo = int(input("Qual vai ser o período de investimento [1 - dia] [2 - mês] [3 - ano?]: "))
tempo = int(input("Digite o tempo que os juros vão render sobre o investimento: "))

if periodo == 1:
    tempo2 = 1
    periodo = "Dia"
elif periodo == 2:
    tempo2 = 30
    periodo = "Mês"
elif periodo == 3:
    tempo2 = 365
    Periodo = "Ano"

tempo3 = tempo * tempo2
juros_acumulados = 0
acumulado = investimento

print(f"Dia      ", end="")
print("Total Investido      ", end="")
print("Juros        ", end="")
print("Total Juros      ", end="")
print("Total acumulado      ",end="")
print()
for i in range (0,tempo3):
    print(f"{i+1}         ", end="")
    print(f" {investimento:.2f}             ", end="")
    print(f"{acumulado * (1 + (juros / 100)) - acumulado:.2f}        ", end="")
    juros_acumulados = juros_acumulados + (acumulado * (1 + (juros / 100)) - acumulado)
    print(f"{juros_acumulados:.2f}             ", end="")
    acumulado = acumulado * (1 + (juros / 100))
    print(f"{acumulado:.2f}")