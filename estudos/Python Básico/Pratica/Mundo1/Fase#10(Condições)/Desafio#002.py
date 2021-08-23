km = int(input('Qual era a velocidade do carro? '))

if km > 80:
    print('Você foi multado!!')
    v = (km - 80) * 7
    print('O valor da multa é de R${}'.format(v))
else:
    print('Tudo certo com a velocidade!')
