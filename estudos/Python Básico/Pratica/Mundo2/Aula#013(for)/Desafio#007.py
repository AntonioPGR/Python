n = int(input('Qual numero quer descobrir se é primo? '))
nd = 0
for c in range(1,n+1):
    if n%c == 0:
        print('\033[33m {} \033[m'.format(c),end=' ')
        nd += 1
    else:
        print('\033[31m {} \033[m'.format(c),end=' ')

print('')
print('Esse numero foi divido por {} numeros'.format(nd))
if nd > 2:
    print('Portanto ele \033[34mNão é primo')
else:
    print('Portanto ele \033[34mé primo')