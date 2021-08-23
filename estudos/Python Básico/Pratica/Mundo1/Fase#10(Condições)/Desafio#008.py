print('-=-'*20)
print('Analisador de triangulos')
print('-=-'*20)

l1 = float(input('Qual a medida do primeiro lado? '))
l2 = float(input('Qual a medida do segundo lado? '))
l3 = float(input('Qual a medida do terceiro lado? '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Eles PODEM formar um triangulo!!')
else:
    print('Eles NÃO PODEM formar um triangulo!!')