lista = []
while True:
    lista.append(int(input('Digite um valor:')))
    if str(input('Deseja continuar?')) in 'Nn':
        break
print(f'Os valores digitados são {lista}')

par = []
impar = []
for c in lista:
    if c%2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Valores pares: {par}')
print(f'Valores impares: {impar}')