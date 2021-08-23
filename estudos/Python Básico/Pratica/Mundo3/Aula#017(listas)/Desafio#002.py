lista = []
while True:
    n = int(input('Qual valor deseja adicionar? '))
    if n not in lista:
        print('Valor adicionado com sucesso!')
        lista.append(n)
    else:
        print('Valor repetido! Não irei adicionar.')

    while True:
        r = str(input('Deseja continuar? [S/N]')).upper()
        if r[0] == 'S' or r[0] == 'N':
            break
        else:
            print('Resposta invalida! use apenas sim ou não!')

    if r[0] == 'N':
        break
lista.sort()
print(f'valores adicionados: {lista}')