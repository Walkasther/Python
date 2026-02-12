# Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
# Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo.

n = int(input('Quantos números voce vai digitar? '))
dentro = fora = 0

for _ in range(n):
    x = int(input('Digite um numero: '))

    if x in range(10, 21):
        dentro += 1
    else:
        fora += 1

print(f'{dentro} DENTRO')
print(f'{fora} FORA')