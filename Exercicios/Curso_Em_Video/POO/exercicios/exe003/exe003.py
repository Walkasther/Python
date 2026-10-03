class ContaBancaria:
    """
    Cria uma conta bancária que faz depósitos e retiradas.
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo


    def depositar(self, deposito):
        self.saldo += deposito
        return f'\033[33mDepósito de R$ {deposito:,.2f} efetuado com sucesso! Saldo atual: {self.saldo}'

    def sacar(self, saque):
        if saque > self.saldo:
            return f'\033[31mSaque de R$ {saque:,.2f} NEGADO! Motivo: Saldo insuficiente.'
        else:
            self. saldo -= saque
            return f'\033[32mSaque de R$ {saque:,.2f} efetuado com sucesso! Saldo atual: {self.saldo}\033[m'


c1 = ContaBancaria(123, 'Mateus', 3000)
print(c1.depositar(500))
print(c1.sacar(5000))
print(c1.sacar(300))
print(c1.__getstate__())

c2 = ContaBancaria(id=121, nome='marcos')
print(c2.depositar(deposito=500))
print(c2)