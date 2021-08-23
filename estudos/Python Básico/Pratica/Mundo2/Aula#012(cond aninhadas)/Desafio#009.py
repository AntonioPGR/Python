v = float(input('Qual o valor do produto?'))
f = int(input("""Forma de pagamento:
Digite 1 para a vista no dinheiro ou cheque;
digite 2 para a vista no cartão;
digite 3 para fazer em até 2 vezes;
digite 4 para 3 vezes ou mais no cartão;
escolha:"""))

if f == 1:
    d = 10/100 * v
    v -= d
    print('O produtor saira com 10% de desconto, portanto o valor sera de R$',v)
elif f == 2:
    d = 5 / 100 * v
    v -= d
    print('O produtor saira com 5% de desconto, portanto o valor sera de R$', v)
elif f == 3:
    print('O produtor saira sem desconto, portanto o valor sera de R$', v)
elif f == 4:
    d = 20 / 100 * v
    v += d
    print('O produtor saira com 20% de juros, portanto o valor sera de R$', v)
