from Desafio001 import moeda

p = float(input('Digite o preço: R$'))
print(f'''A metade de {p} é {moeda.metade(p)}
O dobro de {p} é {moeda.dobro(p)}
Aumentando 10%, temos {moeda.aumentar(p, 10)}
diminuindo 13%, temos {moeda.diminuir(p, 13)}''')