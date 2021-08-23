n1 = float(input('Nota 1:'))
n2 = float(input('Nota 2:'))

m = ( n1 + n2 ) / 2

if m < 5:
    print('REPROVADO!!')
elif m >= 5 and m <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO!!')