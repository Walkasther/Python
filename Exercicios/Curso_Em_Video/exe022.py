#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas.
#O nome com todas as letras em minúsculas.
#Quantas letras ao todo(sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = input('\033[33mQual o seu nome? ').strip()
print(nome.upper())
print(nome.lower())
print(len(''.join(nome.split())))
#print(len(nome) - nome.count(' '))
print('\033[93mO seu primeiro nome é {} e ele tem {} letras'.format(nome.split()[0],len(nome.split()[0])))
print('O seu primeiro nome é {} e ele tem {} letras'.format(nome[0:nome.find(' ')],nome.find(' ')))