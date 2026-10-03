from rich import print
from rich import inspect


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
        return f'Depósito de R$ {deposito:,.2f} efetuado com sucesso! Saldo atual: {self.saldo}'

    def sacar(self, saque):
        if saque > self.saldo:
            return f'Saque de R$ {saque:,.2f} NEGADO! Motivo: Saldo insuficiente.'
        else:
            self. saldo -= saque
            return f'Saque de R$ {saque:,.2f} efetuado com sucesso! Saldo atual: {self.saldo}\033'

#
# c1 = ContaBancaria(123, 'Mateus', 3000)
# print(c1.depositar(500))
# print(c1.sacar(5000))
# print(c1.sacar(300))
# print(c1.__getstate__())

c = ContaBancaria(id=121, nome='marcos')
print(c.depositar(deposito=500))
print(c.depositar(deposito=500))
# print(c)
inspect(c)