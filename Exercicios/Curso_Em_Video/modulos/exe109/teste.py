#modifique as funções criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
#retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from modulos.uteis import leia_float
import moeda

preco = leia_float('Digite um preço: ', positivo=True)

print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preco, 13, True)}')
