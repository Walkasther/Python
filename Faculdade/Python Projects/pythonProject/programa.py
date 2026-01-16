n = int(input("Quantos números serão digitados para somar? "))
soma = 0

for i in range(0, n):
    x = int(input(f"Digite o {i + 1}° número: "))
    soma = soma + x

print("Soma: ", soma)
