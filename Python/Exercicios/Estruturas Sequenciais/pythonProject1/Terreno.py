largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
valor = float(input("Digite o valor do metro quadrado: "))
area = largura * comprimento
preco_final = area * valor

print(f"Area do Terreno: {area:.2f}")
print(f"Preço do Terreno: {preco_final:.2f}")