cod = 0
alcool = 0
gasolina = 0
diesel = 0

while cod != 4 :
    if cod == 1 :
        alcool = alcool + 1
    elif cod == 2:
        gasolina = gasolina + 1
    elif cod == 3:
        diesel = diesel + 1
    cod = int(input("Informe um código (1, 2, 3) ou 4 para parar: "))

print("Muito obrigado!")
print(f"Álcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")