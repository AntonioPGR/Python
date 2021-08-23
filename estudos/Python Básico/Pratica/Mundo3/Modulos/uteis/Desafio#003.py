import d3moeda

p = float(input('Digite o preço:'))
print(f'A metade de {d3moeda.moeda(p)} é {d3moeda.metade(p, True)}')
print(f'O dobro de {d3moeda.moeda(p)} é {d3moeda.dobro(p, True)}')
print(f'Aumentando 10%,temos {d3moeda.aumentar(p, 10, True)}')
print(f'diminuindo 13%,temos {d3moeda.diminuir(p, 13, True)}')