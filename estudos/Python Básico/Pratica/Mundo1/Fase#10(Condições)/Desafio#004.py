km = int(input('Quantos km são de viagem? '))
if km > 200:
    v = km*0.45
    print('O valor é R${}'.format(v))
else:
    v = km*0.5
    print('O valor é R${}'.format(v))