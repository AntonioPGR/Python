tot = 0
barato = ''
maisbarato = 1000000000000000000000000000000000000000000000000
mais1000 = 0

while True:
    print('-'*40)
    print('{: ^40}'.format(' LOJA TOPZERA '))
    print('-' * 40)

    nome = input('Nome do produto:')

    while True:
        p = int(input('Preço do produto:'))
        if p < 0:
            print('Digite valores validos!')
        else:
            break

    if p < maisbarato:
        barato = nome
        maisbarato = p

    tot += p

    if p > 1000:
        mais1000 += 1

    while True:
        r = input('Deseja continuar? [S/N] ').upper().strip()[0]
        if r == 'S' or r =='N':
            break
        else:
            print('Digite valores validos!')

    if r == 'N':
        break

print('---'*15)
print('{:-^40}'.format('LOJA TOPZERA'))
print('---' * 15)

print(f"""O total foi de R${tot}
Temos {mais1000} produtos custando mais de 1000 reais
O produto mais barato foi {barato} custando {maisbarato}""")