nome = input('Digite o seu nome: ').strip()
print('Olá {} {}'.format(nome[:(nome.find(' '))], nome[(nome.rfind(' ') + 1):]))


primo = nome.split()
print('Olá {} {}'.format(primo[0],primo[-1]))


primeiro = nome.split()[0]
ultimo = nome.split()[-1]
resultado = primeiro + ' ' + ultimo
print('Olá',resultado)

print('Olá', primeiro, ultimo)