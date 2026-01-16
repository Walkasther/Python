print("Digite dois números: ")
x = int(input())
y = int(input())

if x > y:
    a = x
    x = y
    y = a

a = 0
for i in range(x+1,y):
    if i % 2 != 0:
        a = a + i

print(f"SOMA DOS IMPARES: {a}")