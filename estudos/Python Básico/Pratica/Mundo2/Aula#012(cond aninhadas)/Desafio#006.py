idd = int(input('Qual a idade do nadador?'))

if idd <= 9:
    print('Mirim')
elif idd <= 14:
    print('Infantil')
elif idd <= 19:
    print('Junior')
elif idd <= 20:
    print('Sênior')
else:
    print('Master')