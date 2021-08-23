n = int(input('Numero:'))
r = int(input('Razão:'))
c = 0
soma = n

while c < 10:
    print(soma, '->', end=' ')
    soma += r
    c += 1
print('Fim')
