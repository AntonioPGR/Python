maior = 0
menor = 1000000
for c in range(0,6):
    p = float(input('Peso da {}° pessoa:'.format(c+1)))
    if p < menor:
        menor = p
    elif p > maior:
        maior = p
print("""Maior Peso: \033[1;31m{}\033[m
Menor Peso: \033[1;36m{}\033[m""".format(maior,menor))