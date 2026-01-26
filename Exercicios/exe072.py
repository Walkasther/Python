#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 até 20.
#Seu o programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete','Oito','Nove','Dez','Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    while n not in range (0,21):
        n = int(input('Tente de novo! Digite um número entre 0 e 20: '))
    print(f'\033[34mVocê digitou o número {tupla[n]}\033[m')
    continuar = input('Quer continuar? [S]Sim/[N]Não: ').strip().upper()[0]
    if continuar == 'N':
        break