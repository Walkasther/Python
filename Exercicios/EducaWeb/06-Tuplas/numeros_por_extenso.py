#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 até 20.
#Seu o programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete','Oito','Nove','Dez','Onze', 'Doze',
         'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    n = int(input('\033[38mDigite um número entre 0 e 20: '))

    if 0 <= n <= 20:
        print(f'\033[34mVocê digitou o  número {tupla[n]}')
        continuar = input('\033[33mQuer continuar? [S]im [N]ão: ').lower().strip()

        if continuar == 's':
            continue
        else:
            break
    else:
        print('\033[31mERRO! O número digitado deve ser entre 0 e 20.')
        continue