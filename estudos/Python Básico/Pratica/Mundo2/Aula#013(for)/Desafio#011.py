somaidd = 0
maisvelho = ''
maioridd = 0
menosvinte = 0
for c in range(0,4):
    print('-------------{}° Pessoa-------------'.format(c+1))
    nome = str(input('Nome:'))
    idd = int(input('idade:'))
    sx = int(input("""[ 1 ] masculino
[ 2 ] feminino
Sexo:""".format(c+1)))

    #media de idade:
    somaidd += idd

    #homem mais velho
    if idd > maioridd:
        maioridd = id
        maisvelho = nome

    #mulheres com menos de 20
    if sx == 2 and idd < 20:
        menosvinte += 1
#---------------------------------
mediaidd = somaidd/4

print('A media das idades é: {}'.format(mediaidd))
print('O homem mais velho é o {} com {} anos'.format(maisvelho, maioridd))
print('E temos {} mulheres com menos de vinte anos.'.format(menosvinte))


