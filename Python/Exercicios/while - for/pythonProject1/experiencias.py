n = int(input("Quantos casos de teste serão digitados? "))
total : int
coelhos = 0
ratos = 0
sapos = 0
pcoelhos = 0
pratos = 0
psapos = 0

for i in range (0,n):
    quantidade = int(input("Quantidade de cobaias: "))
    tipo = input("Tipo de cobaia: ")
    while not (tipo == "c" or tipo == "r" or tipo == "s"):
        print("Tipo não Registrado. Insira um tipo registrado!")
        tipo = input("Tipo de cobaia: ")

    if tipo == "c":
        coelhos = coelhos + quantidade

    elif tipo == "r":
        ratos = ratos + quantidade
    else:
        sapos = sapos + quantidade

total = coelhos + ratos + sapos
pcoelhos = coelhos / total * 100
pratos = ratos / total * 100
psapos = sapos / total * 100

print("\nRELATÓRIO FINAL")
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {pcoelhos:.2f}%")
print(f"Percentual de ratos: {pratos:.2f}%")
print(f"Percentual de sapos: {psapos:.2f}%")