#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('\033[36mDigite o nome: ').strip()
print('\033[96mTem silva no nome? {}'.format('silva' in nome.lower()))
