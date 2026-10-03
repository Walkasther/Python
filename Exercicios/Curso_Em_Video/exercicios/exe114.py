#Crie um código em python que teste se o site Pudim esta acessível pelo computador usado.
import urllib.error
import urllib.request

url = 'https://pudim.com.br/'

try:
    requisicao = urllib.request.Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    site = urllib.request.urlopen(requisicao)

except urllib.error.URLError as erro:
    print('\033[31mO site Pudim não está acessível no momento.\033[m')
    print(f'Erro: {erro}')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')
