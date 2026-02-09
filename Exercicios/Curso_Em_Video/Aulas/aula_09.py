#  Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o
# Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(),
# lower(), capitalize(), title(), strip(), junção com join().

frase = '   Curso em Vídeo Python   '
print(frase)
#mostra apenas o quarto caractere
print(frase[3])
#Mostra do quarto caractere até o décimo segundo
print(frase[3:13])
#Mostra do segundo caractere até o décimo quarto pulando de dois em dois
print(frase[1:15:2])
#Mostra do primeiro até o último caractere
print(frase[:])
#Mostra do primeiro caractere até o décimo segundo
print(frase[:13])
#Mostra do sexto caractere até o último
print(frase[5:])
#Mostra do primeiro ao último caractere pulando de três em três
print(frase[::3])
#Conta quantos caracteres especificos tem na string
print(frase.count('o'))
#Mostra o tamanho da string
print(len(frase))
#Remove os espaços indesejados no início e no final da string
print(len(frase.strip()))
#Cria uma lista com todas as palavras da string
print(frase.split())
#Troca uma palavra na string por outra
print(frase.replace('Python','Android'))
#Verifica se uma palavra está na string
print('Curso' in frase)
#Procura a palavra específica na string e retorna a posição de onde ela começa. Se não encontrar, retorna -1
print(frase.find('Vídeo'))


#Dar um print com mais de uma linha:
print("""Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem
placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus 
fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit 
semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.""")


