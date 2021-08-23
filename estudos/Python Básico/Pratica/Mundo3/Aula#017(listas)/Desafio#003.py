lista = list()

for c in range(0,5):
    n = int(input('Digite um valor:'))

    if c == 0 or n > lista[-1]:
        print('Valor adicionado na ultima posição')
        lista.append(n)
    elif n < lista[0]:
        print('Valor adicionado na primeira posição')
        lista.insert(0,n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na posição {pos}')
                break
            pos += 1

print('-='*30)
print(lista)
