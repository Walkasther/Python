#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
#e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print('{:-^50}'.format('\033[36mEncontrador de Média\033[m'))
z = 's'
cont = maior = menor = soma = 0
while z in 'sS':
    n = int(input('Digite um número inteiro: '))
    cont += 1
    soma += n
    if cont == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    z = input('Quer continuar? [S/n]: ').strip()
media = soma / cont
print('\033[33mA média entre os %i valores digitados é: %.2f'
      '\n\033[32mO maior valor digitado foi %d'
      '\n\033[31mO menor valor digitado foi %i' % (cont,media, maior,menor))