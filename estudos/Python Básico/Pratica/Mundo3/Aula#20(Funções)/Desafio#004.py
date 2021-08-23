from time import sleep
def maior(*num):
    print('-='*20)
    print('Analizando valores....')
    sleep(1)
    print(f'valores passados:', end=' ')
    for k, v in enumerate(num):
        print(v, end=' ')
        sleep(0.5)
        if k == 0:
            maior = v
        elif v > maior:
            maior = v
    print('')
    print(f'Total: {len(num)}')
    print(f'Maior: {maior}')
    print('')


maior(1, 4, 6, 8, 2)
maior(4, 7, 2, 5)
maior(5, 2)
maior(100, 1000, 1000, 5, 7, 5, 4, 2, 3, 0)

