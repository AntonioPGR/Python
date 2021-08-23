from time import sleep


def laco(i, f, p):
    if p == 0:
        p = 1
        print('O passo não pode ser 0, considerarei passo = 1')

    if i > f:
        rp = -p
    else:
        rp = p

    print(f'Contando de {i} até {f} contando de {p} em {p}')
    for c in range(i, f, rp):
        print(c, end=' => ')
        sleep(0.5)
    print('FIM')


print('-='*30)
laco(1, 10, 1)
print('-='*30)
laco(10, 1, 2)
print('-='*30)

print('Agora é sua vez de personalizar a contagem')
ini = int(input('Inicio:'))
fim = int(input('Fim:'))
passo = int(input('Passo:'))
print('-='*30)
laco(ini, fim, passo)
