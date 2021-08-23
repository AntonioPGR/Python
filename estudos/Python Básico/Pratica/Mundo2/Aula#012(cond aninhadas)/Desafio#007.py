l1 = int(input('Lado 1:'))
l2 = int(input('Lado 2:'))
l3 = int(input('Lado 3:'))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Eles podem formar triângulo!')

    if l1 == l2 and l2 == l3 and l3 == l1:
        print('E eles formam um triângulo equilatero')
    elif l1 != l2 and l2 != l3 and l3 != l1:
        print('E eles formam um triangulo escaleno')
    else:
        print('E eles formam um triangulo isósceles')

else:
    print('Eles Não podem formar triangulo!')