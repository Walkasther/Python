#Faça um program que leia três números e mostre qual é o maior e qual é o menor.
from time import process_time_ns

n1 = int(input('número 1: '))
n2 = int(input('número 2: '))
n3 = int(input('número 3: '))
maior = int
menor = int

if n1 > n2:
    if n1 > n3:
        maior = n1
        if n2 > n3:
            menor = n3
        else:
            menor = n2
    else:
        maior = n3
        menor = n2
else:
    if n2 > n3:
        maior = n2
        if n1 > n3:
            menor = n3
        else:
            menor = n1
    else:
        maior = n3
        menor = n1
print('\033[1;103;34mEntre os números digitados, o maior é {} e o menor é {}\033[m'.format(maior,menor))
