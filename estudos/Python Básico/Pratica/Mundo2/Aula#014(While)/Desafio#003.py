teste = 0
n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
while teste == 0:
    esc = int(input('''     Temos os numeros: \033[34m{}\033[m e \033[34m{}\033[m, aperte para:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair
    escolha:'''.format(n1,n2)))

    if esc == 1:
        print('A soma é: \033[31m',n1 + n2,'\033[m')
    elif esc == 2:
        print('A multiplicação é \033[31m',n1*n2,'\033[m')
    elif esc == 3:
        if n1 > n2:
            print('O maior é: \033[31m',n1,'\033[m')
        else:
            print('O maior é: \033[31m',n2,'\033[m')
    elif esc == 4:
        n1 = int(input('Digite um numero:'))
        n2 = int(input('Digite outro numero:'))
    elif esc == 5:
        teste = 1
print('FIM')
