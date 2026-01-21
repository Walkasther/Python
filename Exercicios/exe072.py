#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 até 20.
#Seu o programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete','Oito','Nove','Dez','Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
n = int(input('Digite um número entre 0 e 20: '))
while n not in range (0,21):
    n = int(input('Tente de novo! Digite um número entre 0 e 20: '))
print(f'Você digitou o número {tupla[n]}')
