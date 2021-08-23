nuns = ('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    n = int(input('Digite um numero inteiro entre 0 e 10:'))
    if n < 11 and n >= 0:
        break
    print('Tente novamente,',end=' ')

print(f'Voce digitou o numero {nuns[n]}')