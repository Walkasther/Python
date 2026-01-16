from iqoptionapi.stable_api import IQ_Option
import time

# Configurações iniciais
email = 'mateuswalkasther@gmail.com'
senha = 'Iq#2015'
valor_inicial = 2
multiplicador = 2.2
usar_conta_real = False  # Defina como True para usar a conta real, False para conta de treinamento
tipo = 'digital'
ativo = "EURUSD-OTC"
meta_diaria = 200

# Conectar à plataforma IQ Option
iq = IQ_Option(email, senha)
iq.connect()

# Verificar conexão
if iq.check_connect():
    print("Conectado com sucesso!")
else:
    print("Erro ao conectar")
    exit()

# Selecionar conta
if usar_conta_real:
    iq.change_balance("REAL")
    print("Usando conta real.")
else:
    iq.change_balance("PRACTICE")
    print("Usando conta de treinamento.")

def aguardar_fechamento_vela(periodo=60):
    tempo_atual = int(time.time())
    segundos_restantes = periodo - (tempo_atual % periodo)
    print('-'*100)
    print(f"\nAguardando {segundos_restantes} segundos para a vela fechar...")
    time.sleep(segundos_restantes)

def obter_ultimas_velas(iq, ativo, periodo=60, quantidade=1):
    try:
        aguardar_fechamento_vela(periodo)
        velas = iq.get_candles(ativo, periodo, quantidade, time.time())
        if not velas:
            raise ValueError("Nenhuma vela foi retornada pela API")
        
        cores = []
        for vela in velas:
            if vela['close'] > vela['open']:
                cores.append('verde')
            elif vela['close'] < vela['open']:
                cores.append('vermelha')
            else:
                cores.append('doji')
        return cores
    except Exception as e:
        print(f"Erro ao obter velas: {e}")
        return []

def verificar_padrao_intercalado(cores):
    if len(cores) < 1:
        return False
    for i in range(0):
        if cores[i] == cores[i+1]:
            return False
    return True


# Função principal de trading
def trading():
    valor = valor_inicial
    total_win = 0
    total_loss = 0
    lucro2 = 0
    maior_win = 0
    maior_loss = 0
    n_operacao = 1
    maior_n_operacao = 0
    sequencia_win = 0
    maior_sequencia_win = 0
    trocador = 0
    
    while True:
        cores = obter_ultimas_velas(iq, ativo)
        if not cores:
            print("Erro ao obter velas, tentando novamente...")
            time.sleep(60)
            continue
        
        print(f"Últimas velas fechadas: {cores}")
        
        if verificar_padrao_intercalado(cores):
            ultima_cor = cores[-1]
            direcao = 'call' if ultima_cor == 'vermelha' else 'put'
            break
        time.sleep(0.1)

    direcao1 = direcao
    direcao2 = 'call' if direcao1 =='put' else 'put'
    
    
    #while lucro2 <= meta_diaria:
    while True:
        for direcao in [direcao1, direcao2]:
            #status -> essa variavel vai receber true ou false, indicando se a transação foi feita ou não
            #id -> Retorna o id da transação caso a variavel check for  true, ou um erro caso não de para abrir uma transação    
            status, id = iq.buy_digital_spot_v2(ativo,valor, direcao, 1) if tipo == 'digital' else iq.buy(valor, ativo, direcao, 1)      

            if status: 
                print('#' * 20)
                print(f"\nOperação {direcao} com valor R$ {valor:.2f} realizada com sucesso.")
                # Verificar resultado da operação
                while True:
                    time.sleep(0.1)
                    status, lucro = iq.check_win_digital_v2(id) if tipo == 'digital' else iq.check_win_v4(id)
                    if status:
                        if lucro > 0:
                            print(f"\n>>Operação {direcao} ganhou. Lucro: {lucro:.2f} \n>>N° da operação: {n_operacao}")
                            valor = valor_inicial  # Resetar valor após ganho
                            total_win = total_win + lucro
                            n_operacao = 1
                            sequencia_win += 1
                            trocador = 0
                            if maior_win < lucro:
                                maior_win = lucro
                        elif lucro == 0:
                            print(f"\n>>Operação {direcao} empatou. Saldo: {lucro:.2f} \n>>N° da operação: {n_operacao}")
                            trocador = 2
                        else:
                            print(f"\n>>Operação {direcao} perdeu. Perda: {lucro:.2f} \n>>N° da operação: {n_operacao}")
                            valor *= multiplicador  # Multiplicar valor após perda
                            total_loss = total_loss + lucro
                            n_operacao = n_operacao + 1
                            sequencia_win = 0
                            trocador += 1
                            if maior_loss > lucro:
                                maior_loss = lucro

                        lucro2 = total_win + total_loss
                        if maior_n_operacao < n_operacao:
                            maior_n_operacao = n_operacao 
                        if maior_sequencia_win < sequencia_win:
                            maior_sequencia_win = sequencia_win
                        print(f'\nTotal Win: {total_win:.2f} \nTotal Loss: {total_loss:.2f} \nLucro atual: {lucro2:.2f} \nMaior WIN: {maior_win:.2f} \nMaior LOSS: {maior_loss:.2f} \nMaior n° de operação: {maior_n_operacao} \nMaior sequencia Win: {maior_sequencia_win} \nMaior sequencia Loss: {maior_n_operacao - 1}')
                        break
            else:
                print(f"Erro ao realizar operação {direcao}. Tentando novamente...", id)
                time.sleep(60)  # Esperar 1 minuto antes da próxima operação
            if trocador == 2:
                direcao1 = 'put' if direcao1 == 'call' else 'call' 
                direcao2 = 'put' if direcao2 == 'call' else 'call'
                trocador = 0  # Reseta contador de perdas seguidas
                print("\n>> Padrão de intercalação alterado!")
                break
        


# Iniciar trading
trading()