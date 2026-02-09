#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('\033[35mDigite o nome da cidade: ').strip()

#Solução 1
print('\033[95mComeça com santo? {}'.format(cidade[:5].lower() == 'santo'))
#Solução 2
print('Começa com santo? {}'.format('santo' in cidade.lower().split()[0]))
#Solução 3
santo = cidade.lower().split()
print('Começa com santo? {}'.format('santo' in santo[0]))

print(cidade.lower().split()[0])

