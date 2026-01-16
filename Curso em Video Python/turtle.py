nome = 'Mateus douglas de azevedo serafim'

print(nome.capitalize())
print(nome.title())
print(nome.upper())
print(nome.lower())
print(len(nome.split()[0]))
separado = nome.split()

print(separado[0])
junto = ''.join(separado)
print(junto)
print('Possui {} caracteres excluindo os espaços.'.format(len(junto)))
print('O primeiro nome tem {} letras.'.format(len(separado[0])))
