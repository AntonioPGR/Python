n = int(input('digite um numero de 0 a 9999:'))
print('Unidade: {}'.format(n // 1 % 10))
print('Dezena: {}'.format(n // 10 % 10))
print('Centena: {}'.format(n // 100 % 10))
print('Milhar: {}'.format(n // 1000 % 10))



