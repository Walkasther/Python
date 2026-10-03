#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
#novamente até ter um valor correto.

sexo = str(input('\033[34m[M]MASCULINO '
             '\n\033[35m[F]FEMININO'
             '\n\033[30;107mInforme o sexo da pessoa:\033[m')).upper().strip()[0]

while not sexo in 'MF':
        sexo = input('\033[91mEntrada invalida!! digite uma opção valida [M/F]: ').upper().strip()
print('\033[mO sexo informado foi: %s' % ('\033[34mMasculino' if sexo == 'M' else '\033[35mFeminino'))
