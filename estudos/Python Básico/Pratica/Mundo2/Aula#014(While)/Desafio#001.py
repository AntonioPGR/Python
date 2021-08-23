c = 0
while c == 0:
    sx = str(input('Qual seu sexo? [F/M] ')).upper().strip()
    if sx == 'M' or sx == 'F':
        c = 1
    else:
        c = 0
        print('Digitação errada, tente novamente!')
print('Fim')