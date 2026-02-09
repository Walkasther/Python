#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
#999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
#(desconsiderando o flag).
a = b = 0
c = int(input('Digite um número inteiro [999 para parar]: '))
while c != 999:
    a += c
    b += 1
    c = int(input('Digite um número inteiro [999 para parar]: '))
print('Foram digitados %d números, e a soma entre eles é %i' % (b,a))
