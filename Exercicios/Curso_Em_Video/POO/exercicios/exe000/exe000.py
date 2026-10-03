# ============================================================
# EXERCÍCIO 1
# Crie a classe Gafanhoto e instancie 3 objetos com nome e idade,
# exibindo a mensagem de cada um usando o método mensagem().
# ============================================================

class Gafanhoto:
    def __init__(self):
        self.nome = ''
        self.idade = 0


    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é um Gafanhoto(a) e tem {self.idade} anos de idade.'


g1 = Gafanhoto()
g1.nome = 'Maria'
g1.idade = 17

g2 = Gafanhoto()
g2.nome = 'Maikon'
g2.idade = 43

g3 = Gafanhoto()
g3.nome = 'Kim'
g3.idade = 14

print(g1.mensagem())
print(g2.mensagem())
print(g3.mensagem())


# ============================================================
# EXERCÍCIO 2
# Crie um objeto Gafanhoto, exiba sua mensagem com valores padrão,
# depois altere seus atributos e exiba novamente.
# ============================================================

g4 = Gafanhoto()
print(g4.mensagem())
g4.nome = 'Lira'
g4.idade = 24
print(g4.mensagem())


# ============================================================
# EXERCÍCIO 3
# Crie um objeto com idade inicial 10, chame o método
# aniversario() cinco vezes e mostre a idade final.
# ============================================================

g5 = Gafanhoto()
g5.idade = 10
g5.aniversario()
g5.aniversario()
g5.aniversario()
g5.aniversario()
g5.aniversario()
print(g5.mensagem())



# ============================================================
# EXERCÍCIO 4
# Crie dois objetos com idades diferentes, faça apenas um deles
# fazer aniversário e mostre as mensagens de ambos.
# ============================================================

g6 = Gafanhoto()
g6.idade = 20

g7 = Gafanhoto()
g7.idade = 30
g7.aniversario()

print(g6.mensagem())
print(g7.mensagem())



# ============================================================
# EXERCÍCIO 5
# Crie um objeto sem alterar atributos e exiba a mensagem
# para observar os valores padrão definidos no construtor.
# ============================================================

g8 = Gafanhoto()
print(g8.mensagem())


# ============================================================
# EXERCÍCIO 6
# Crie três objetos, atribua nome e idade para cada um,
# armazene-os em uma lista e percorra-a exibindo mensagem().
# ============================================================

o1 = Gafanhoto()
o2 = Gafanhoto()
o3 = Gafanhoto()

o1.nome = 'João'
o1.idade = 5
o2.nome = 'Juninho'
o2.idade = 7
o3.nome = 'Jéssica'
o3.idade = 9

pessoas = [o1, o2, o3]

for pessoa in pessoas:
    print(pessoa.mensagem())


# ============================================================
# EXERCÍCIO 7
# Teste o comportamento do self chamando aniversario()
# em G1 duas vezes e em G2 uma vez, confirmando os estados.
# ============================================================

g1.aniversario()
g1.aniversario()
g2.aniversario()
print(g1.mensagem())
print(g2.mensagem())

# ============================================================
# EXERCÍCIO 8
# Crie um objeto, exiba a mensagem com nome vazio,
# atribua um nome depois e exiba novamente.
# ============================================================

obj = Gafanhoto()
print(obj.mensagem())
obj.nome = 'Mirian'
print(obj.mensagem())

# ============================================================
# EXERCÍCIO 9
# Crie um objeto e atribua propositalmente uma idade negativa
# para perceber que, sem encapsulamento, o código aceita tudo.
# ============================================================

idade_negativa = Gafanhoto()
idade_negativa.idade = -18

print(idade_negativa.mensagem())

# ============================================================
# EXERCÍCIO 10
# Crie 4 objetos com nome e idade e exiba as mensagens
# em ordem crescente de idade (manualmente, sem sort automático).
# ============================================================

o7 = Gafanhoto()
o7.nome = 'João'
o7.idade = 5
o6 = Gafanhoto()
o6.nome = 'Juninho'
o6.idade = 7
o5 = Gafanhoto()
o5.nome = 'Jéssica'
o5.idade = 9
o4 = Gafanhoto()
o4.nome = 'Jéssica'
o4.idade = 11

print(o7.mensagem())
print(o6.mensagem())
print(o5.mensagem())
print(o4.mensagem())