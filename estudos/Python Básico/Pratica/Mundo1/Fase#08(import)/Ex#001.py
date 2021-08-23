import math

num = int(input('digite um numero:'))
raiz = math.sqrt(num)
print('A raiz de {} é {:.4f}'.format(num, raiz))
print('A raiz de {} arredondada para cima é: {}'.format(num, math.ceil(raiz)))
print('A raiz de {} arredondada para baixo é: {}'.format(num, math.floor(raiz)))