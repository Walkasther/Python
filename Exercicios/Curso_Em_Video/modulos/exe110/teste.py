#Adicione ao módulo da moeda.py uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções
#que já temos no módulo criado até aqui.

from modulos.uteis import leia_float
import moeda

preco = leia_float("Digite um preço: ", True)

moeda.resumo(preco, 80, 35)
