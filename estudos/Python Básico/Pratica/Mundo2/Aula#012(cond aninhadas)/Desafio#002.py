
n = int(input('Digite o numero que deseja converter:'))
b = int(input("""Digite 1 para converter para binário
Digite 2 para converter para octal
Digite 3 para converter para hexadecimal
escolha:"""))

if b == 1:
    print('Convertendo {} para binario fica {}'.format(n, bin(n)[2:]))
elif b == 2:
    print('Convertendo {} para octal fica {}'.format(n, oct(n)[2:]))
elif b == 3:
    print('Convertendo {} para hexadecimal fica {}'.format(n, hex(n)[2:]))
else:
    print('Digito invalido!')