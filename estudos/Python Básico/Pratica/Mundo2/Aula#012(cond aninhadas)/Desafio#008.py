a = float(input('Qual sua altura? (em metros)'))
p = float(input('Qual seu peso?'))
imc = p / (a**2)

if imc < 18.5:
    print('Seu imc é {:.2f} portanto voce esta abaixo do peso!!'.format(imc))
elif imc < 25:
    print('Seu imc é {:.2f} portanto voce está com peso ideal!!'.format(imc))
elif imc < 30:
    print('Seu imc é {:.2f} portanto voce está´com sobrepeso!!'.format(imc))
elif imc < 40:
    print('Seu imc é {:.2f} portanto voce está com obesidade!!'.format(imc))
else:
    print('Seu imc é {:.2f} portanto voce está com obesidade morbida!!'.format(imc))