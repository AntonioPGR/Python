lista = []
while True:
    lista.append(int(input('Digite um valor:')))
    if str(input('Deseja continuar?'))[0].upper() == 'N':
        break
print(f'Os valores digitados foram: {lista}')

lista.sort(reverse=True)
print(f'os valores em ordem decrescente são: {lista}')

if 5 in lista:
    print(f'O valor 5 está na lista e esta na posição {lista.index(5)}')
else:
    print('O valor 5 não está na lista de valores')