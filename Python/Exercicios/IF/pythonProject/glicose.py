quantidade = float(input("Digite a medida da glicose: "))

if quantidade <= 100:
    classificacao = "Normal"
elif quantidade <= 140:
    classificacao = "Elevado"
else:
    classificacao = "Diabetes"

print("Classificacao: ",classificacao)
