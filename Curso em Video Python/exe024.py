cidade = input('qual o nome da cidade? ')

santo = cidade.split()[0]
print('santo' in santo.lower())
print((cidade[:5].lower() == 'santo'))
