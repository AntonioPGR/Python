while True:
    n = int(input('Quer ver a tabuada de qual valor?'))
    if n < 0:
        break
    print('---'*15)
    c = 0
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('---' * 15)
    print('Escreva um valor negativo para parar!')
    print('---' * 15)
print('FIM')