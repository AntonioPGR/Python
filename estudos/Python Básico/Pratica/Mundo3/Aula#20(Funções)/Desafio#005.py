from random import randint
from time import sleep

def sorteia(num):
    print('-='*20)
    print('Sorteando Valores...')
    print('-=' * 20)
    sleep(0.5)
    print(f'Os valores sorteados são:', end=' ')
    for c in range(0,5):
        n = randint(1, 10)
        num.append(n)
        sleep(0.5)
        print(n, end=' ')
    print('')

def somapar(num):
    print('-=' * 20)
    print('Analizando Valores Sorteados...')
    print('-=' * 20)
    s = 0
    for v in num:
        if v%2 == 0:
            s += v
    sleep(1)
    print(f'A soma dos valores pares é: {s}')


numeros = list()
sorteia(numeros)
somapar(numeros)