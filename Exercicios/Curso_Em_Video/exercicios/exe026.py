#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece pela última vez.

frase = input('\033[37mDigite uma frase: ').strip().lower()

print('\033[90mA frase possui {} a(s)'.format(frase.count('a')))
print('O primeiro a começa na posição {}'.format(frase.find('a')))
print('O último a está na posição {}'.format(frase.rfind('a')))
