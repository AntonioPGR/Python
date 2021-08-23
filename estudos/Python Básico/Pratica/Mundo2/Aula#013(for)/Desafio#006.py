i = int(input('Inicio:'))
p = int(input('Razão:'))
for c in range(0,10):
    if c != 9:
        print(i,'->',end=' ')
    else:
        print(i, '-> FIM')
    i += p