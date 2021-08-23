from random import randint
print('-_-'*10)
print('Jogo do adivinho')
print('-_-'*10)
print('Pense em um numero ente  0 e 10! Duvido você acertar!')
p = int(input('Seu palpite: '))
n = randint(0,10)
tnt = 1
while p != n:
    tnt += 1
    print('==='*5)
    print('Voce errou!')
    if p > n:
        print('Menos...Tente Denovo!')
    elif p < n:
        print('Mais...Tente Denovo!')
    p = int(input('Seu palpite: '))
    print('===' * 5)
print("""Voce Acertouu!!!!
-------------
Resumo:
-------------
Numero escolhido pelo computador: {}
Numero de tentativas: {}""".format(n,tnt))


