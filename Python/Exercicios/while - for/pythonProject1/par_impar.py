n = int(input("Quantos numeros voce vai digitar? "))

for i in range (0,n):
    x = int(input("Digite um numero: "))

    if x == 0:
        print("NULO")
    elif x % 2 == 0:
        print("PAR" , end=" ")
    else:
        print("IMPAR", end=" ")
    if x < 0:
        print("NEGATIVO")
    elif x > 0:
        print("POSITIVO")