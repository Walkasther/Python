#Crie um programa que leia uma frase e diga se ela é um palíndromo, desconsiderando os espaços.
#ex de palíndromo: apos a sopa

from unidecode import unidecode
frase = input('Digite uma frase: ').strip().lower()
palindromo = False
a = unidecode(''.join(frase.split()))
print(a)
for i in range (0,len(a)):
    palindromo = a[i] == a[len(a)-1-i]
    if not palindromo:
        break

if palindromo:
    print('\033[32mEssa frase é um palíndromo!')
else:
    print('\033[31mEssa frase não é um palíndromo!')