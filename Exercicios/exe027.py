#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
#Ex: Ana Maria de Souza
#Primeiro: Ana
#Último: Souza

nome = input('\033[97mQual o seu nome? ').strip()
#solução 1
print('Primeiro: {}\nÚltimo:   {}'.format(nome.split()[0],nome.split()[-1]))
#Solução2
n = nome.split()
print(f'Primeiro: {n[0]}\nÚltimo: {n[len(n)-1]}')

