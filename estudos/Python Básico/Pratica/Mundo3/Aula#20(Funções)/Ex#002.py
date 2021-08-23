def contador(*num):
    tam = len(num)
    print(f'Numero de valores: {tam}')
    for c in num:
        print(c, end=' ')
    print('Fim')
    tam = len(num)



contador(1, 2, 6)
contador(2, 6)
contador(2, 5, 7, 8, 2, 4)