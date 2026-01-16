print("Digite as idades: ")
idade = int(input())

if idade < 0:
    print("IMPOSSÍVEL CALCULAR")
else:
    media = 0
    c = 0
    while idade >= 0:
        c = c + 1
        media = media + idade
        idade = int(input())

    media = media / c
    print(f"MÉDIA = {media:.2f}")