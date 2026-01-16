duracao = int(input("Digite a duracao em segundos: "))
hora = int(duracao / 3600)
minuto = int((duracao - hora * 3600) / 60)
segundo = int((duracao - hora * 3600) - (minuto * 60))

print(f"{hora}:{minuto}:{segundo}")