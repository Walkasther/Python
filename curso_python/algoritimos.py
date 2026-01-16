# nome = 'Mateus Douglas'
# altura = 1.75
# peso = 88
# imc = peso / altura**2

# print(nome, 'tem', altura, 'de altura, \npesa', peso, 'quilos e \nseu imc é', imc)

# #format
# print('{} tem {} de altura, \npesa {} quilos e \nseu imc é {:.2f}'.format(nome, altura, peso, imc))

# a = 2
# b = 'b'
# c = 1.1
# string = 'a={} b={} c={:.2f}'
# formato = string.format(a,b,c)
# print(formato)

# primeiro_valor = input('Digite o primeiro valor: ')
# segundo_valor = input('Digite o segundo valor: ')

# # if primeiro_valor > segundo_valor:
#     print(f'O primeiro valor {primeiro_valor} é maior que o segundo {segundo_valor}')
# elif primeiro_valor < segundo_valor:
#     print('O segundo valor {1} é maior que o primeiro {0}'.format(primeiro_valor, segundo_valor))
# else:
#     print('Os dois valores', primeiro_valor, 'e', segundo_valor, 'são iguais')

# if 0:
#     print('Verdadeiro')

# nome = 'mateus'

# print(nome[-1::-1])

# nome3 = input('Digite seu nome: ')
# idade = int(input('Digite sua idade: '))
# a = 'Você pode beber' if idade >= 18 else a = 'Você é menor de idade'
# print(a)

# ARDUINO = 20

# if idade and nome3:
   
#     print(f'Seu nome é {nome3}')
#     print(f'Seu nome invertido é {nome3[-1::-1]}')
# #    print(f'Seu nome invertido é {nome[::-1]}')
#     print(f'Seu nome tem {len(nome3)} letras')
#     print(f'A primeira letra do seu nome é {nome3[0]}')
#     print(f'A última letra do seu nome é {nome3[-1]}')
#  #   print ('Seu nome contem espaços') if ' ' in nome else print ('Seu nome não contém espaços')
#     print ('Seu nome contem espaços' if ' ' in nome3 else 'Seu nome não contém espaços')
# else:
#     print('Desculpe, você deixou campos vazios.')

velocidade = 61
local_carro = 100

RADAR_1     =   60
LOCAL_1     =   100
RADAR_RANGE =   1


antes               =   LOCAL_1 - RADAR_RANGE
depois              =   LOCAL_1 + RADAR_RANGE
acima_da_velocidade =   velocidade > RADAR_1
antes_do_radar_1    =   local_carro >= (antes)
depois_no_radar_1   =   local_carro <= (depois)
passou_no_radar_1   =   antes_do_radar_1 and depois_no_radar_1
levou_multa         =   passou_no_radar_1 and acima_da_velocidade

if acima_da_velocidade:
    print('Carrou passou do limite de velocidade do radar 1')

if levou_multa:
    print('Carrou levou multa no radar 1')




