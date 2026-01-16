"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
# """
# try:
#     numero = int(input("digite um numero inteiro: "))

#     if numero % 2 == 0:
#         print("o número digitado é par")
#     else: 
#         print("o número digitado é impar")
# except:
#     print("Você não digitou um numero inteiro")

# """
# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
# descrito, exiba a saudação apropriada. Ex. 
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
# """
# try:
#     hora = float(input("Olá, que horas são agora? "))
#     if hora <= 11:
#         print('Bom dia!')
#     elif hora >= 12 and hora <=17:
#         print('Boa tarde!')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite!')
#     else:
#         print('Você não digitou um horário válido')

# except:
#     print('Você não digitou um horário válido')

# """
# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
# "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
# """

# nome = input('Ditite o seu nome: ')
# print(f'O seu nome tem {len(nome)} letras, portanto,')
# caracteres = len(nome)


# if caracteres < 5:
#     print('seu nome é curto')
# elif caracteres == 5 or caracteres == 6:
#     print('seu nome é normal')
# else:
#     print('seu nome é muito grande')

a = 7.0 // 2
print(a)