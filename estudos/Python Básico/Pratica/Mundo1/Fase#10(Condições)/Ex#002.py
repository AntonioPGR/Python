n1 = float(input('Nota 1:'))
n2 = float(input('Nota 2:'))
m = (n1+n2)/2
if m >= 7:
    print('sua média foi {}, então você passou de ano!!'.format(m))
else:
    if m >= 5:
        print('sua média foi {}, então você esta de recuperação'.format(m))
    else:
        print('sua média foi {}, então você bombou de ano!!'.format(m))