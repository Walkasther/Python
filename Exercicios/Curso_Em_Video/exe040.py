#Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, conforme a média atingida:
#-Média abaixo de 5.0: REPROVADO
#-Média entre 5.0 e 6.9: RECUPERAÇÃO
#-Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m =  float('%.1f' % ((n1 + n2) / 2))
print('Média: %.1f \nStatus: ' % m, end='')
if m >= 7:
    print('\033[92mAPROVADO')
elif m < 5:
    print('\033[91mREPROVADO')
else:
    print('\033[93mRECUPERAÇÃO')
