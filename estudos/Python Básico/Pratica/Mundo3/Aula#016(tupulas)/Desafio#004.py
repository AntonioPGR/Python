#n1 = int(input('Digite um valor:'))
#n2 = int(input('Digite um valor:'))
#n3 = int(input('Digite um valor:'))
#n4 = int(input('Digite um valor:'))
#t = (n1, n2, n3, n4)

t = (int(input('Digite um valor:')),
     int(input('Digite um valor:')),
    int(input('Digite um valor:')),
    int(input('Digite um valor:')))

print(f'Numeros digitados {t}')

print(f'O numero 9 apareceu {t.count(9)} vezes')
if 3 in t:
    print(f'O valor 3 apareceu na {t.index(3)} posição')
else:
    print('O valor 3 não foi digitado')

print('Os numeros pares digitados foram:',end=' ')
for cn, c  in enumerate(t):
    if c%2==0:
        print(c,end=' ')
