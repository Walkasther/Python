#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
#999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles(Desconsiderando o flag).


n = s = c = 0
print(f'{'\033[32mSomador de números\033[m':-^50}')
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    s += n
    c +=1
print(f'\033[34mForam digitados {c} números, e a soma entre eles é {s}')