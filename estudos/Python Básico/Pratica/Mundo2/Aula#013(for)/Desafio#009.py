maior = 0
menor = 0
for c in range(0,7):
    idd = int(input('Idade do {}° candidato:'.format(c+1)))
    if idd >= 21:
        maior += 1
    else:
        menor += 1
print('Maior: {}'.format(maior),end=' ')
print('Menor: {}'.format(menor))