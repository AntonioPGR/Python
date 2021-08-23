import random
print('Pensei em um numero entre 0 e 3, duvido você acertar!')
print('-=-'*20)
ne = int(input('Qual seu chute? '))
print('-=-'*20)
nr = random.randint(1,3)
if ne > 3:
    print('Numero invalido, tente novamente com numeros validos')
else:
    if ne == nr:
        print('Perdi!!O numero era {}, portanto você acertou!!'.format(nr))
    else:
        print('Ganhei!!O numero era {}, portanto você errou!!'.format(nr))