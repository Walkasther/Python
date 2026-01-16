n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2)

if media < 60:
    print(f"NOTA FINAL: {media}")
    print("REPROVADO!")
else:
    print(f"NOTA FINAL: {media}")