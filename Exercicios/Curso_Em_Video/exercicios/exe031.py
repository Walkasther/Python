#Desenvolva um programa que pergunte a distância de uma viagem em km. Cobrando 0,50 por km para viagens de até 200km
#e 0,45 para viagens mais longas.

print('\033[33mPassagem: \nR$ 0,50 até 200km\nR$ 0,45 acima de 200km\033[m')
d = input('\033[4;106;97mQual o valor da distância? km:\033[m')
d2 = int(d)
# if d2 <= 200:
#     passagem = d2 * 0.5
#     print('Passagem: R$ 0,50 por km')
#
# else:
#     passagem = d2 * 0.45
#     print('Passagem: 0,45 por km')
#
# print('O valor da passagem é R$ {:.2f}'.format(passagem))

print('O preço da passagem é R$ {:.2f}'.format(d2 * 0.5 if d2 <= 200 else d2 *0.45))