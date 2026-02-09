#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('\033[31mQual o comprimento da primeira reta? '))
b = float(input('\033[32mQual o comprimento da segunda reta? '))
c = float(input('\033[33mQual o comprimento da terceira reta? '))

# if a + b > c:
#     if b + a > c:
#         if b + c > a:
#             print('Com essas três retas é possível formar um triângulo retângulo :)')
#         else:
#             print('Com essas três retas não é possível formar um triângulo retângulo :(')
#     else:
#         print('Com essas três retas não é possível formar um triângulo retângulo :(')
# else:
#             print('Com essas três retas não é possível formar um triângulo retângulo :(')

if a < b + c and b < a + b and c < a + b:
    print('\033[42;97mÉ possível formar um triângulo com essas retas.\033[m')
else:
    print('\033[44;97mNão é possível formar um triângulo com essas retas.\033[m')