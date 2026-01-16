print("Digite dois números inteiros:  ")
a = int(input())
b = int(input())

if (a >= b and a%b == 0) or (b > a and b%a == 0):
    print("São multiplos")
else  :
       print("Não são multiplos")