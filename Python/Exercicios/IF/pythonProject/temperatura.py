temperatura = input("Voce vai digitar a temperatura em qual escala (C/F)? ")

if temperatura == "f":
    n = float(input(f"Digite a temperatura em Fahrenheit: "))
    c = 5 / 9 * (n-32)
    print(f"Temperatura equivalente em Celsius: {c:.2f}")
else:
    n = float(input(f"Digite a temperatura em  Celsius: "))
    f = 9 * n / 5 + 32
    print(f"Temperatura equivalente em Fahrenheit: {f:.2f}")

