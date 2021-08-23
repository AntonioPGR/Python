from math import sqrt,factorial

num = int(input('digite um numero:'))
raiz = sqrt(num)
print('A raiz de {} é: {:.2f}'.format(num, raiz))
fat = factorial(num)
print('O fatorial de {} é: {}'.format(num, fat))