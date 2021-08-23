n = int(input('Numero:'))
r = int(input('Razão:'))
f = 10
#c = 0 aki vai mostrar so o q add
#soma = 0
resp = 1
while resp != 0:
    c = 0
    soma = 0
    while c < f:
        soma += n
        print(soma, '->', end=' ')
        c += 1
    print('Fim')
    if resp != 0:
        resp = int(input('Deseja mostrar mais quantos termos? [0 para finalizar]:'))
    f += resp