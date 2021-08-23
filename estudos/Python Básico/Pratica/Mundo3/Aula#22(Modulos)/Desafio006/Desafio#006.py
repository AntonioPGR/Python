from Desafio006.dados import dados
from Desafio006.moeda import moeda

p = dados.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 80, 35)