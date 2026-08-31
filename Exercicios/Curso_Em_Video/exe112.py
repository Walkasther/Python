#Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
#leia_dinheiro() que seja capaz de funcionar como a função input, más com uma validação de dados para aceitar apenas
#valores que sejam monetários.

from utilidadesCeV import moeda
from utilidadesCeV.dado import leia_dinheiro

preco = leia_dinheiro('Digite um Preço: R$',True)
moeda.resumo(preco,35,22)