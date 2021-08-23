from Desafio002 import moeda

p = float(input('Digite o preço: R$'))
print(f'''A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}
O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}
Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}
diminuindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}''')