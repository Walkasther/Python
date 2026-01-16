from iqoptionapi.stable_api import IQ_Option
import time
from configobj import ConfigObj
import json, sys

#registrar com e-mail e senha
#email = 'mateuswalkasther@gmail.com'
#senha = 'Iq#2015'
config = ConfigObj('config.txt')
email = config['LOGIN']['email']
senha = config['LOGIN']['senha']

valor_inicial = config['AJUSTES']['valor_inicial']
multiplicador = config['AJUSTES']['multiplicador']
tipo_de_conta = False # Defina como True para usar a conta real, False para conta de treinamento

ativo = 'EURUSD'
direcao = 'call'
exp = 1
tipo = 'digital'


API = IQ_Option(email,senha)

#logar na corretora e checar a conexão
check, reason = API.connect()
if check:
    print('Conectado com Sucesso!')
else:
    if reason == '{"code":"invalid_credentials","message":"You entered the wrong credentials. Please ensure that your login/password is correct."}':
        print('Email ou senha incorreto.')
    else:
        print('Houve um problema na conexão :(')
        print(reason)
        sys.exit()

#Escolher Tipo de conta demo ou real
if tipo_de_conta:
    conta = 'REAL'
else:
    conta = 'PRACTICE'
print('Usando conta', conta)

API.change_balance(conta)

#Função para compra ou venda
def compra(ativo,valor_inicial,direcao,exp,tipo):
    if tipo == 'digital':
        check, id = API.buy_digital_spot_v2(ativo,valor_inicial,direcao,exp)
    else:
        check, id = API.buy(valor_inicial,ativo,direcao,exp)

    #verificar se conseguiu abrir a ordem
    if check:
        print('Ordem executada!', id)

        while True:
            time.sleep(0.1)
            status, resultado = API.check_win_digital_v2(id) if tipo == 'digital' else API.check_win_v4(id)

            #Só entra nesse if se o status retornar true
            #Significa que ja deu o resultado da operação
            if status:
                #se o resultado for maior que 0 quer dizer que deu WIN
                if resultado > 0:
                     print('WIN', round(resultado,2))
                # se o resultado for igual a 0 quer dizer que deu empate a operação
                elif resultado == 0:
                    print('EMPATE', round(resultado,2))
                # se o resultado for menor que 0 quer dizer que deu LOSS
                else:
                    print('LOSS', round(resultado,2))
                break

    else:
        print('Erro na abertura da ordem,', id)

compra(ativo,valor_inicial,direcao,exp,tipo)

