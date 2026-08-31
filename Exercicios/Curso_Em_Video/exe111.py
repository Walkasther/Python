# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
#Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo funcionando.

from modulos.uteis import leia_float
from utilidadesCeV import moeda

preco = leia_float('Digite um Preço: R$',True)
moeda.resumo(preco,35,22)