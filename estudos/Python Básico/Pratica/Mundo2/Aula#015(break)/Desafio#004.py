mais18 = 0
hcadast = 0
menos20 = 0
while True:
    print('CADASTRE UMA PESSOA')
    print('--'*15)
    while True:
        idd = int(input('Idade:'))
        if idd >= 0:
            break
        else:
            print('Digite valores validos')

    while True:
        sx = str(input('Sexo: [M/F}')).upper().strip()[0]
        if sx == 'M' or sx == 'F':
            break
        else:
            print('Digite valores validos!')
    print('--' * 15)
    if idd > 18:
        mais18 += 1
    if sx == 'M':
        hcadast += 1
    if sx == 'F' and idd < 20:
        menos20 += 1

    while True:
        r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if r == 'S' or r == 'N':
            break
        else:
            print('Digite valores validos!')
    print('--' * 15)
    if r == 'N':
        break

print(f"""Temos {mais18} pessoas com mais de 18 anos
Temos {hcadast} homens cadastrados
Temos {menos20} mulheres cadastradas com menos de 20 anos""")