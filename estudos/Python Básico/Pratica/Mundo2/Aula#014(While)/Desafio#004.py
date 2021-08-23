f = int(input('Numero:'))
c = f
fat = 1
print('Calculando 6! =',end=' ')
while c != 1:
    fat = fat*c
    print(f'{c} x', end=' ')
    c -= 1
    print('=',end=' ')
print(fat)