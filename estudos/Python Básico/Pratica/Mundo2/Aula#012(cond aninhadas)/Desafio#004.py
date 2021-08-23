from datetime import date

ano = int(input('Quando você nasceu?'))
anoat = date.today().year

idd = anoat - ano

if idd < 18:
    f = 18 - idd
    print('faltam {} para você se alistar!'.format(f))
elif idd > 18:
    f = idd - 18
    print('Fazem {} anos que você se alistou ou deveria ter se alistado!'.format(f))
else:
    print('Você deve se alistar esse ano')
