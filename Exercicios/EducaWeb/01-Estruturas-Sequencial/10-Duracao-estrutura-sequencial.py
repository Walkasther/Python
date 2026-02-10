#Fazer um programa para ler uma duração de tempo em segundos, daí imprimir na tela esta duração no formato
#horas:minutos:segundos.

duracao = int(input('Digite a duração em segundos: '))

horas = duracao // 3600
minutos = (duracao - (horas * 3600)) // 60
segundos = duracao - (minutos * 60) - (horas * 3600)

print(f'{horas:02d}:{minutos:02d}:{segundos:02d}')
