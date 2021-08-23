n = int(input('quantos numeros deseja mostrar:'))
n1 = 0
n2 = 1
c = 0
while c < n:
    print('{} ->'.format(n1), end=' ')
    soma = n1 + n2
    n1 = n2
    n2 = soma
    c += 1
print('FIM')
