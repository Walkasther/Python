n = int(input("Quantos casos voce vai digitar? "))

for i in range (0,n):
    print("Digite 3 números")
    x = float(input())
    y = float(input())
    z = float(input())
    media = ((x * 2) + (y * 3) + (z * 5)) / ( 2 + 3 + 5)
    print(f"MÉDIA = {media:.1f}")

