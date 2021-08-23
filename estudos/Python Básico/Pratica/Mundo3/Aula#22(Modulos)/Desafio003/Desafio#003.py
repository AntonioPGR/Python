from Desafio003 import moeda

p = float(input('Digite o preço: R$'))
print(f'''A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}
O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}
Aumentando 10%, temos {moeda.aumentar(p, 10, True)}
diminuindo 13%, temos {moeda.diminuir(p, 13, True)}''')