c = 0
soma = 0
ndig = 0
while c != 999:
    v = int(input('Digite um numero: [Para finalizar digite 999]:'))
    if v == 999:
        c = 999
    else:
        soma += v
        ndig += 1
print('Você digitou {} valores, e a soma deles é: {}'.format(ndig,soma))