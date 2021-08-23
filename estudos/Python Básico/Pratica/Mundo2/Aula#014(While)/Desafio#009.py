nval = soma = maior = menor = 0
c = 'S'
while c.upper() == 'S':
    n = int(input('Qual numero deseja adicionar? '))
    c = str(input('Deseja adicionar mais um valor? [S/N]'))
    if nval == 1:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    nval += 1
med = soma / nval

print('''O maior valor é: {}
O menor valor é: {}
A média entre eles é: {}'''.format(maior,menor,med))